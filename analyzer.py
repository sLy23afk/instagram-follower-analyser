import json
from tabulate import tabulate
import csv
import os

with open('followers_1.json', 'r') as f:
    followers_data = json.load(f)
    
with open('following.json', 'r') as f:
    following_raw = json.load(f)
    following_data = following_raw['relationships_following'
                                   ]
with open('recently_unfollowed_profiles.json', 'r') as f:
    recently_unfollowed_raw = json.load(f)
    recently_unfollowed = recently_unfollowed_raw["relationships_unfollowed_users"]
    
followers = [entry["string_list_data"][0]["value"] for entry in followers_data]
following = [entry["string_list_data"][0]["value"] for entry in following_data]
unfollowed =[entry["string_list_data"][0]["value"] for entry in recently_unfollowed]
print("🔁 Followers:")
for name in followers:
    print("-", name)

print("\n➡️ People You Follow:")
for name in following:
    print("-", name)

print("fkin retards that lost")
for name in unfollowed:
    print('-', name)

    
followers_set = set(followers)
following_set = set(following)
unfollowed_set = set(unfollowed)

not_following = following_set - followers_set
fansss = followers_set - following_set

print("\n🚫 People You Don't Follow Back:")
for person in not_following:
    print("-", person)
print("\n Usual fans lmao:")
for person in fansss:
    print("-", fansss)
    
table = [
    ["Followers", len(followers)],
    ["following", len(following)],
    ["Not Following You Back", len(not_following)],
    ["LMFAO UNFOLLOWED", len(unfollowed_set)],
    ["You Don't Follow Back", len(fansss)]
]


print("\n📊 Summary Table:\n")
print(tabulate(table, headers=["Category", "Count"], tablefmt="grid"))
    
    
with open("results.txt", 'w') as file:
    file.write("People who Don't Follow Back:\n")
    for person in not_following:
        file.write(f"- {person}\n")
with open('results.txt', 'w') as file:
    file.write("I dont give a fuck bout:\n")
    for person in fansss:
        file.write(f"- {person}\n")
with open('results.txt', 'w') as file:
    file.write("Dumbasses i Unfollowed lmao:\n")
    for person in unfollowed_set:
        file.write(f"- {person}\n")
        
print('\n Results saved in the results.txt!')


max_rows = max(len(followers), len(following), len(not_following), len(unfollowed_set), len(fansss))
followers_list = list(sorted(followers)) + [""] * (max_rows - len(followers))
following_list = list(sorted(following)) + [""] * (max_rows - len(following))
unfollowed_list = list(sorted(unfollowed_set)) + [""] * (max_rows - len(unfollowed_set))
not_following_back_list = list(sorted(not_following)) + [""] * (max_rows - len(not_following))
fans_list = list(sorted(fansss)) + [""] * (max_rows - len(fansss))
detailed_table = []
for i in range(max_rows):
    row = [
        followers_list[i],
        following_list[i],
        not_following_back_list[i],
        unfollowed_list[i],
        fans_list[i]
    ]
    detailed_table.append(row)
print("\n📋 Detailed User Table:\n")
print(tabulate(
    detailed_table,
    headers=["Followers", "Following", "Fkin retards","LMFAO UNFOLLOWED", "Fansss"],
    tablefmt="grid"
))

if os.path.exists('detailed_results.csv'):
    os.remove('detailed_results.csv')
with open('detailed_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Followers", "Following", "Not Following You Back","LMFAO UNFOLLOWED", "Fans"])  # Header

    for row in detailed_table:
        writer.writerow(row)

print("\n✅ Detailed results exported to detailed_results.csv!")
