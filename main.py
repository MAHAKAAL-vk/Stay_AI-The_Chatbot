# from backend.memory.chroma_memory.add_data import add_pdf_to_chroma
# from backend.Conversations.chat import chat_with_travel_assistant
import uvicorn
from backend.App.api import app


if __name__ == "__main__":

    uvicorn.run(app, host="localhost", port=8000)

    # chat_with_travel_assistant()

    # agent = BrowserAgent()
    # queries = "Give me an itinery for a 4 day tour to Banglore"#,"Give me a proper plan to survive in UP for 10 day as a tourist.""Give me a plan for a 3 days trip to Jaipur.",
    # agent.run(queries)

    # tool = BrowserTool()
    # results = tool.search("Give me some information about places to visit in Jaipur")
    # snippets = tool.get_snippets_from_search_results(results)
    # summary = tool.summarize_snippets(snippets)
    # print(summary)

    # base_path = r"C:\Users\vicky\OneDrive\Desktop\Projects\Infosys_Internship_Project\StayAI\Dataset"
    # pdf_files = [
    #     "\Andhra_Pradesh.pdf","\Arunachal_Pradesh.pdf","\Assam.pdf","\Bihar.pdf","\Chhattisgarh.pdf","\Goa.pdf","\Gujarat.pdf","\Haryana.pdf","\Himachal_Pradesh.pdf","\India.pdf",
    #     "\Jharkhand.pdf","\Karnataka.pdf","\Madhya_Pradesh.pdf","\Maharashtra.pdf","\Manipur.pdf","\Meghalaya.pdf","\Mizoram.pdf","\\Nagaland.pdf","\Odisha.pdf","\Punjab.pdf",
    #     "\Rajasthan.pdf","\Sikkim.pdf","\Tamil_Nadu.pdf","\Telangana.pdf","\Tripura.pdf","\\UT_Andaman_and_Nicobar_Islands.pdf","\\UT_Chandigarh.pdf","\\UT_Dadra_and_Nagar_Haveli_and_Daman_and_Diu.pdf",
    #     "\\UT_Delhi.pdf","\\UT_Jammu_and_Kashmir.pdf","\\UT_Ladakh.pdf","\\UT_Lakshadweep.pdf","\\UT_Puducherry.pdf","\\Uttar_Pradesh.pdf","\\Uttarakhand.pdf","\\West_Bengal.pdf",
    # ]
    # pdf_paths = [base_path + pdf_file for pdf_file in pdf_files]
    # for pdf_path in pdf_paths:
    #     add_pdf_to_chroma(pdf_path)