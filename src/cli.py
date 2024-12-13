import argparse
import logging
from src.model_loader import load_model
from src.code_assistant import process_code

# Set up logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    parser = argparse.ArgumentParser(description="AI Code Assistant CLI")
    parser.add_argument(
        "--mode",
        type=str,
        choices=["generate", "review", "optimize", "document"],
        required=True,
        help="Specify the mode of operation: generate, review, optimize, document"
    )
    parser.add_argument(
        "--input_file",
        type=str,
        help="Path to the input file containing code"
    )
    parser.add_argument(
        "--output_file",
        type=str,
        default="output.txt",
        help="Path to the output file where results will be saved"
    )
    args = parser.parse_args()

    # Load the model
    logging.info("Loading model...")
    model = load_model("codellama-7b")

    if not model:
        logging.error("Failed to load model.")
        print("Error: Unable to load the model.")
        return

    # Process the input code
    try:
        logging.info(f"Processing code in {args.mode} mode...")
        with open(args.input_file, "r") as file:
            code = file.read()
        result = process_code(model, code, args.mode)

        with open(args.output_file, "w") as file:
            file.write(result)
        print(f"Results saved to {args.output_file}")
        logging.info(f"Results saved to {args.output_file}")

    except Exception as e:
        logging.error(f"Error processing code: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
