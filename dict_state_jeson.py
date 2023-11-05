import json
dict_state={
  "Andhra Pradesh": "Amaravati",
  "Karnataka": "Bengaluru",
  "Tamil Nadu": "Chennai",
  "Maharashtra": "Mumbai",
  "Delhi": "New Delhi",
  "Rajasthan": "Jaipur",
  "Uttar Pradesh": "Lucknow"
}

with open("state.json","w") as f:
    capitals=json.dump(dict_state,f)
    
    