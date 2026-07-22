from load_image import ft_load


def main():
    """Main execution of the tests for load_image."""
    print("----- Test 1: Subject Test Case (Valid Image) -----")
    print(ft_load("landscape.jpg"))

    print("\n----- Test 2: Non-existent Image File -----")
    print(ft_load("nonexistent.jpg"))

    print("\n----- Test 3: Invalid Type for Path -----")
    print(ft_load(123))  # type: ignore


if __name__ == "__main__":
    main()
