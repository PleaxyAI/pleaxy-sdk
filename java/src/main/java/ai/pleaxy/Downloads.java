package ai.pleaxy;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;

/**
 * Saves a file download (a payment export's CSV, a remittance advice PDF) to a temporary file. The generated API
 * classes call it in place of openapi-generator's JSON parsing of a binary body (scripts/fix-generated.mjs).
 */
public final class Downloads {
  private Downloads() {}

  /** Copies the stream to a new temporary file, deleted when the JVM exits, and closes the stream. */
  public static File toTempFile(InputStream body) throws IOException {
    Path file = Files.createTempFile("pleaxy-", ".download");
    file.toFile().deleteOnExit();
    try (InputStream in = body) {
      Files.copy(in, file, StandardCopyOption.REPLACE_EXISTING);
    }
    return file.toFile();
  }
}
