import random

def generate_payloads(count: int):
    """Generate random payloads in the desired hex format."""
    payloads = []
    for _ in range(count):
        payload = ''.join([f"\\x{random.choice('0123456789abcdef')}{random.choice('0123456789abcdef')}" for _ in range(64)])
        payloads.append(payload)
    return ''.join(payloads)  # Join payloads without spaces

def main():
    print("👋 Welcome to the Payload Generator!")

    try:
        count = int(input("🔢 Enter the number of payloads you want (up to 10,000): "))

        if 1 <= count <= 10000:
            print(f"🔄 Generating {count} payloads. Please wait...\n")
            payloads = generate_payloads(count)
            print(payloads)  # Print all payloads in one line without spaces
            print(f"\n✅ Successfully generated {count} payloads.")
        else:
            print("❌ Please enter a number between 1 and 10,000.")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()