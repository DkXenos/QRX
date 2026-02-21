import qrcode
import os
import sys


def get_desktop_path() -> str:
    return os.path.join(os.path.expanduser("~"), "Desktop")


def generate_qr_code(url: str, filename: str) -> None:

    desktop = get_desktop_path()
    if not filename.lower().endswith(".jpg"):
        filename = filename + ".jpg"
    output_path = os.path.join(desktop, filename)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    img.save(output_path, format="JPEG")
    print(f"\n✅ QR code saved successfully!\n   Path: {output_path}")


def main() -> None:
    print("=== CLI QR Code Generator ===\n")

    url = input("Enter the URL or link to encode: ").strip()
    if not url:
        print("❌ Error: URL cannot be empty.", file=sys.stderr)
        sys.exit(1)

    filename = input("Enter the output filename (without extension): ").strip()
    if not filename:
        print("❌ Error: Filename cannot be empty.", file=sys.stderr)
        sys.exit(1)

    desktop = get_desktop_path()
    if not os.path.isdir(desktop):
        print(
            f"❌ Error: Desktop directory not found at '{desktop}'.",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        generate_qr_code(url, filename)
    except Exception as exc:
        print(f"❌ Error generating QR code: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
