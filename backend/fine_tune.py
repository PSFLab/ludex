from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI()


fine_tune_start = client.fine_tuning.jobs.create(
    training_file="file-MVynK1ztgcXud8dwdwt2ps",
    model="gpt-4o",
)

print(fine_tune_start)

result = client.fine_tuning.jobs.list_events(
  fine_tuning_job_id="ftjob-h1MJXwtH4KwWfoK3C3EpCJlw")

for elem in result:
    print(result)


