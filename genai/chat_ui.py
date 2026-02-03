from chat_with_data import chat

while True:
    q = input("Ask data question (or 'exit'): ")
    if q.lower() == "exit":
        break

    try:
        rows = chat(q)
        for r in rows:
            print(r)
    except Exception as e:
        print("❌ Error:", e)
