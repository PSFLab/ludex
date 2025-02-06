import json

with open("doc.txt", "r", encoding="utf-8") as doc_file:
    document_text = doc_file.read().strip()

with open("judge_summary.txt", "r", encoding="utf-8") as summary_file:
    judge_summary = summary_file.read().strip()

prompt_text = (
    "Document:\n" + document_text +
    "\n\nPlease provide a judge-style summary:"
)

training_example = {
    "prompt": prompt_text,
    "completion": " " + judge_summary
}

with open("training_data.jsonl", "w", encoding="utf-8") as outfile:
    json_line = json.dumps(training_example, ensure_ascii=False)
    outfile.write(json_line + "\n")