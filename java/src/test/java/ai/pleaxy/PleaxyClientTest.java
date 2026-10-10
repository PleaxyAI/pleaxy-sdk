package ai.pleaxy;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import ai.pleaxy.client.ApiException;
import ai.pleaxy.model.ApiError;
import ai.pleaxy.model.CancelPurchaseOrderInput;
import ai.pleaxy.model.GetPurchaseOrderResult;
import ai.pleaxy.model.PurchaseOrder;
import com.sun.net.httpserver.HttpServer;
import java.io.File;
import java.lang.reflect.Method;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

class PleaxyClientTest {
  private HttpServer server;
  private final List<Map<String, String>> seen = new ArrayList<>();

  private String serve(int status, String contentType, String body) throws Exception {
    server = HttpServer.create(new InetSocketAddress("127.0.0.1", 0), 0);
    server.createContext("/", exchange -> {
      String requestBody = new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8);
      seen.add(Map.of(
          "method", exchange.getRequestMethod(),
          "uri", exchange.getRequestURI().toString(),
          "apiKey", String.valueOf(exchange.getRequestHeaders().getFirst("X-Api-Key")),
          "authorization", String.valueOf(exchange.getRequestHeaders().getFirst("Authorization")),
          "body", requestBody));
      byte[] bytes = body.getBytes(StandardCharsets.UTF_8);
      exchange.getResponseHeaders().set("Content-Type", contentType);
      exchange.sendResponseHeaders(status, bytes.length);
      exchange.getResponseBody().write(bytes);
      exchange.close();
    });
    server.start();
    return "http://127.0.0.1:" + server.getAddress().getPort() + "/";
  }

  @AfterEach
  void stop() {
    if (server != null) server.stop(0);
  }

  @Test
  void sendsTheApiKeyToTheWorkspaceUrl() throws Exception {
    String base = serve(200, "application/json", "{\"id\":\"PO-1\",\"status\":\"draft\",\"someNewField\":1}");
    PleaxyClient client = PleaxyClient.builder().baseUrl(base).apiKey("key.secret").workspaceId("reg_123.buyer").build();
    GetPurchaseOrderResult result = client.purchaseOrders().getPurchaseOrder("PO-1", "reg_9.buyer");
    assertEquals("GET", seen.get(0).get("method"));
    assertEquals("/v1/workspaces/reg_123.buyer/purchase-orders/PO-1?buyer=reg_9.buyer", seen.get(0).get("uri"));
    assertEquals("key.secret", seen.get(0).get("apiKey"));
    PurchaseOrder po = (PurchaseOrder) result.getActualInstance();
    assertEquals("PO-1", po.getId());
  }

  @Test
  void sendsAJsonBodyWithASessionToken() throws Exception {
    String base = serve(201, "application/json", "{\"id\":\"PO-1\"}");
    PleaxyClient client = PleaxyClient.builder().baseUrl(base).accessToken("tok").workspaceId("w").build();
    PurchaseOrder po = client.purchaseOrders().cancelPurchaseOrder("PO-1", new CancelPurchaseOrderInput().reason("duplicate"));
    assertEquals("POST", seen.get(0).get("method"));
    assertEquals("/v1/workspaces/w/purchase-orders/PO-1/cancel", seen.get(0).get("uri"));
    assertEquals("Bearer tok", seen.get(0).get("authorization"));
    assertEquals("{\"reason\":\"duplicate\"}", seen.get(0).get("body"));
    assertEquals("PO-1", po.getId());
  }

  @Test
  void readsTheApiErrorCode() throws Exception {
    String base = serve(409, "application/json", "{\"statusCode\":409,\"code\":\"PO_ID_AMBIGUOUS\",\"message\":\"Two buyers issued PO-1\"}");
    PleaxyClient client = PleaxyClient.builder().baseUrl(base).apiKey("k").workspaceId("w").build();
    ApiException e = assertThrows(ApiException.class, () -> client.purchaseOrders().getPurchaseOrder("PO-1", null));
    assertEquals(409, e.getCode());
    ApiError error = client.error(e).orElseThrow();
    assertEquals("PO_ID_AMBIGUOUS", error.getCode());
    assertEquals("Two buyers issued PO-1", error.getMessage().getActualInstance());
  }

  @Test
  void returnsAFileDownload() throws Exception {
    String base = serve(200, "text/csv; charset=utf-8", "invoice,amount\nINV-1,10\n");
    PleaxyClient client = PleaxyClient.builder().baseUrl(base).apiKey("k").workspaceId("w").build();
    File csv = client.invoices().getPaymentExport("EXP-1");
    assertEquals("invoice,amount\nINV-1,10\n", Files.readString(csv.toPath()));
  }

  @Test
  void requiresAWorkspaceAndACredential() {
    assertThrows(IllegalArgumentException.class, () -> PleaxyClient.builder().apiKey("k").build());
    assertThrows(IllegalArgumentException.class, () -> PleaxyClient.builder().workspaceId("w").build());
  }

  @Test
  void hasAnAccessorForEveryApiArea() throws Exception {
    File apiDir = new File("src/main/java/ai/pleaxy/api");
    for (String file : apiDir.list()) {
      String api = file.replace(".java", "");
      String accessor = Character.toLowerCase(api.charAt(0)) + api.substring(1, api.length() - "Api".length());
      Method method = PleaxyClient.class.getMethod(accessor);
      assertEquals("ai.pleaxy.api." + api, method.getReturnType().getName());
    }
    assertTrue(Arrays.stream(PleaxyClient.class.getMethods()).anyMatch(m -> m.getName().equals("purchaseOrders")));
  }
}
