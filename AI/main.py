from tool import data_extraction
from llm import llm
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

financial_document = "AI/Apex Solutions LLC.pdf"

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You will be analyzing a financial document to calculate total income, total expenses, and net income. Here is the financial document:

            {financial_document}

            Your task is to carefully review this document and extract all relevant financial information to calculate:

            1. Total Income: The sum of all money received or earned.
            2. Total Expenses: The sum of all costs, charges, and outgoing payments.
            3. Net Income: The difference between total income and total expenses.

            Please follow these steps:

            1. Analyze the document thoroughly, identifying all sources of income and all expenses.

            2. Use a <scratchpad> to show your calculations. List each income item and expense item you identify, along with its amount. Then show the totals for income and expenses, and the calculation for net income.

            3. After your calculations, provide your final answer in the following format:

            <answer>
            Total Income: [Amount in dollars]
            Total Expenses: [Amount in dollars]
            Net Income: [Amount in dollars]
            </answer>

            Make sure to include the dollar sign ($) and use commas for thousands where appropriate in your final answer.

            If you encounter any ambiguities or if there's information that seems unclear, state your assumptions clearly in the scratchpad before making calculations based on them.

            Remember, accuracy is crucial in financial calculations. Double-check your math and make sure you haven't missed any items from the document.
    """
        ),MessagesPlaceholder(variable_name="financial_document")
    ]
)

financial_data = data_extraction(dir=financial_document)
chain = prompt | llm | StrOutputParser()

response = chain.invoke(
        {
         "financial_document": [HumanMessage(content=financial_data)]
         },
    )

print(response)