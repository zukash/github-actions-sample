import os

def main():
    name = os.environ.get('INPUT_NAME', 'World')
    greeting = f"Hello, {name}!"
    print(f"::set-output name=greeting::{greeting}")

if __name__ == "__main__":
    main()