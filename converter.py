import sys
import os
import pypandoc



def convert_file(input_path: str, output_path: str, to_format: str) -> bool:
    """
    Logic to convert documents between formats using pypandoc.
    """
    
    if not os.path.isfile(input_path):
        print(f"Error: File '{input_path}' does not exist.")
        return False

    try:
        pypandoc.convert_file(input_path, to_format, outputfile = output_path)
        return True

    except FileNotFoundError:
        print(f"Oops! Couldn't find the file '{input_path}'. Try again.")
        return False

    except OSError as e: 
        print(f"Error: Conversion failed. Format '{to_format}' may not be supported. Details: {e}")
        return False

    except Exception as e:
        print(f"Unexpected error during conversion: {e}")
        return False


def main():
    """
    Main entry point for CLI usage.
    Expected usage:
        python converter.py input.docx output.pdf pdf
    """

    # TODO 4: Parse sys.argv for input_path, output_path, to_format
    if len(sys.argv) != 4:
        print("Usage: python converter.py <input_path> <output_path> <to_format>")
        print("Example: python converter.py input.docx output.pdf pdf")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    to_format = sys.argv[3]
    
    print(f"Converting '{input_path}' to '{to_format}'")
    success = convert_file(input_path, output_path, to_format)
    
    if success:
        print(f"Conversion successful! Output saved to '{output_path}'")
    else:
        print("Conversion failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()