import os
from typing import Dict
from your_framework import (
    register_tool,
    ActionContext,
    PythonActionRegistry,
    Agent,
    Goal,
    PythonEnvironment,
    AgentFunctionCallingActionLanguage,
    prompt_expert,
    prompt_llm_for_json,
    generate_response,
)

# === Tool: Categorization Expert ===
@register_tool(tags=["invoice_processing", "categorization"])
def categorize_expenditure(action_context: ActionContext, description: str) -> str:
    categories = [
        "Office Supplies", "IT Equipment", "Software Licenses", "Consulting Services", 
        "Travel Expenses", "Marketing", "Training & Development", "Facilities Maintenance",
        "Utilities", "Legal Services", "Insurance", "Medical Services", "Payroll",
        "Research & Development", "Manufacturing Supplies", "Construction", "Logistics",
        "Customer Support", "Security Services", "Miscellaneous"
    ]
    return prompt_expert(
        action_context=action_context,
        description_of_expert="A senior financial analyst with deep expertise in corporate spending categorization.",
        prompt=f"Given the following description: '{description}', classify the expense into one of these categories:\n{categories}"
    )

# === Tool: Purchasing Rules Validator ===
@register_tool(tags=["invoice_processing", "validation"])
def check_purchasing_rules(action_context: ActionContext, invoice_data: dict) -> dict:
    rules_path = "config/purchasing_rules.txt"
    try:
        with open(rules_path, "r") as f:
            purchasing_rules = f.read()
    except FileNotFoundError:
        purchasing_rules = "No rules available. Assume all invoices are compliant."

    validation_schema = {
        "type": "object",
        "properties": {
            "compliant": {"type": "boolean"},
            "issues": {"type": "string"}
        }
    }

    return prompt_llm_for_json(
        action_context=action_context,
        schema=validation_schema,
        prompt=f"""
        Given this invoice data: {invoice_data}, check whether it complies with company purchasing rules.
        The latest purchasing rules are as follows:

        {purchasing_rules}

        Respond with a JSON object containing:
        - `compliant`: true if the invoice follows all policies, false otherwise.
        - `issues`: A brief explanation of any violations or missing requirements.
        """
    )

# === Invoice Agent Definition ===
def create_invoice_agent():
    action_registry = PythonActionRegistry()
    goals = [
        Goal(
            name="Persona",
            description="You are an Invoice Processing Agent, specialized in handling invoices efficiently."
        ),
        Goal(
            name="Process Invoices",
            description="""
            Your goal is to process invoices accurately. For each invoice:
            1. Extract key details such as vendor, amount, and line items.
            2. Generate a one-sentence summary of the expenditure.
            3. Categorize the expenditure using an expert.
            4. Validate the invoice against purchasing policies.
            5. Store the processed invoice with categorization and validation status.
            6. Return a summary of the invoice processing results.
            """
        )
    ]
    environment = PythonEnvironment()
    return Agent(
        goals=goals,
        agent_language=AgentFunctionCallingActionLanguage(),
        action_registry=action_registry,
        generate_response=generate_response,
        environment=environment
    )

# === Example Invoice Test ===
if __name__ == "__main__":
    invoice_text = """
        Invoice #4567
        Date: 2025-02-01
        Vendor: Tech Solutions Inc.
        Items: 
          - Laptop - $1,200
          - External Monitor - $300
        Total: $1,500
    """

    agent = create_invoice_agent()
    response = agent.run(f"Process this invoice:\n\n{invoice_text}")
    print(response)
