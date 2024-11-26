import pandas as pd
import altair as alt

# Define the services offered
services = {
    "Social media management": {
        "description": "Manage and optimize social media accounts",
        "price": 2000  # Monthly price in MXN
    },
    "Content creation": {
        "description": "Create engaging content for social media",
        "price": 3000  # Monthly price in MXN
    },
    "Graphic design": {
        "description": "Design visually appealing graphics for social media",
        "price": 2500  # Monthly price in MXN
    },
    "Marketing strategy": {
        "description": "Develop a comprehensive social media marketing strategy",
        "price": 5000  # Monthly price in MXN
    },
    "Competitor analysis": {
        "description": "Analyze competitors' social media presence and strategies",
        "price": 1500  # Monthly price in MXN
    },
    "Community management": {
        "description": "Engage with followers and build a strong online community",
        "price": 2500  # Monthly price in MXN
    },
    "Number of posts": {
        "description": "Number of social media posts per month",
        "price_per_post": 100  # Price per post in MXN
    },
    "Content complexity": {
        "description": "Complexity of social media content (e.g., basic, advanced)",
        "price_per_level": 500  # Price per complexity level in MXN
    },
    "Number of channels": {
        "description": "Number of social media channels managed",
        "price_per_channel": 500  # Price per channel in MXN
    },
    "Reporting frequency": {
        "description": "Frequency of social media performance reports (e.g., monthly, quarterly)",
        "price_per_frequency": 250  # Price per reporting frequency in MXN
    }
}

# Define packages
packages = {
    1: {
        "name": "Basic",
        "services": ["Social media management", "Content creation", "Number of posts"],
        "content_complexity": "Basic",
        "num_channels": 2,
        "reporting_frequency": "Monthly"
    },
    2: {
        "name": "Standard",
        "services": ["Social media management", "Content creation", "Graphic design", "Competitor analysis", "Number of posts"],
        "content_complexity": "Intermediate",
        "num_channels": 3,
        "reporting_frequency": "Monthly"
    },
    3: {
        "name": "Premium",
        "services": ["Social media management", "Content creation", "Graphic design", "Marketing strategy", "Community management", "Number of posts"],
        "content_complexity": "Advanced",
        "num_channels": 5,
        "reporting_frequency": "Monthly"
    }
}

def recommend_packages(company_size):
    """Recommends packages based on company size."""
    if company_size == "small":
        return [1, 2]
    elif company_size == "medium":
        return [2, 3]
    elif company_size == "large":
        return [3]
    else:
        return [1, 2, 3]

def calculate_package_details(package_id, num_posts):  # Add num_posts as argument
    """Calculates total cost, client cost, and profit for a package."""
    package_details = packages[package_id]
    total_cost = 0
    for service in package_details["services"]:
        if "price" in services[service]:
            total_cost += services[service]["price"]

    # Calculate cost of posts based on the provided num_posts
    total_cost += num_posts * services["Number of posts"]["price_per_post"]

    if "Content complexity" in package_details:
        complexity_levels = {"Basic": 1, "Intermediate": 2, "Advanced": 3}
        total_cost += complexity_levels[package_details["content_complexity"]] * services["Content complexity"]["price_per_level"]
    if "Number of channels" in package_details:
        total_cost += package_details["num_channels"] * services["Number of channels"]["price_per_channel"]
    if "Reporting frequency" in package_details:
        total_cost += services["Reporting frequency"]["price_per_frequency"]

    # Define expenses (replace with your actual expenses)
    expenses = {
        "Jasper.ai (Pro)": 1032.50,
        "Buffer (Essentials)": 210,
        "Other expenses": 500
    }

    total_expenses = sum(expenses.values())
    client_cost = total_cost * 1.5  # Example: 50% markup
    profit = client_cost - total_expenses

    return {
        "total_cost": total_cost,
        "client_cost": client_cost,
        "profit": profit
    }

def main():
    while True:
        # Get company size from the user with validation
        while True:
            company_size = input("Enter company size (small, medium, large): ").lower()
            if company_size in ["small", "medium", "large"]:
                break
            else:
                print("Invalid input. Please enter 'small', 'medium', or 'large'.")

        # Recommend packages
        recommended_packages = recommend_packages(company_size)
        print("\nRecommended packages:")
        for package_id in recommended_packages:
            included_services = packages[package_id]["services"]
            services_str = ", ".join(included_services)
            print(f"{package_id}. {packages[package_id]['name']} (Includes: {services_str})")

        # Get package selection from the user with validation
        while True:
            try:
                selected_package_id = int(input("\nEnter the number of the selected package: "))
                if selected_package_id in packages:
                    break
                else:
                    print("Invalid package selection. Please enter a valid package number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Get the desired number of posts per month with validation
        while True:
            try:
                num_posts = int(input("Enter the desired number of posts per month: "))
                if num_posts > 0:
                    break
                else:
                    print("Invalid input. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Calculate and display package details
        package_details = calculate_package_details(selected_package_id, num_posts)
        print("\nPackage details:")
        print(f"  Total cost of resources: ${package_details['total_cost']:.2f} MXN")
        print(f"  Cost for the client: ${package_details['client_cost']:.2f} MXN")
        print(f"  Profit: ${package_details['profit']:.2f} MXN")

        # Ask if the user wants to restart or exit
        restart = input("\nDo you want to restart? (yes to restart, any other key to exit): ").lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()