from intent_parser import parse_intent
from sql_generator import generate_sql
from db_executor import run_query

def chat(query: str):
    intent = parse_intent(query)
    sql = generate_sql(intent)
    return run_query(sql)
