import json

def mask_email(email):
    parts = email.split('@')
    return parts[0][0] + "***@" + parts[1]

def main():
    with open('toxic_sample.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    cleaned_data = []
    seen_ids = set()
    for record in data:
        record_id = record.get('id')
        if record_id in seen_ids:
            continue
        
        price = record.get('price', 0)
        if price < 0 or price > 5000:
            continue
        
        seen_ids.add(record_id)
        
        if 'name' in record:
            del record['name']
        
        if 'email' in record:
            record['email'] = mask_email(record['email'])
            
        cleaned_data.append(record)
    
    with open('sanitized_sample.json', 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, indent=4)
        
    print(f"Từ {len(data)} bản ghi ban đầu, còn lại {len(cleaned_data)} bản ghi hợp lệ.")

if __name__ == "__main__":
    main()
