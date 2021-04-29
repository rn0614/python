partyA={"Park", "Kim", "Lee"}
partyB={"Park", "길동" ,"몽룡"}

C=partyA&partyB

print("파티에 참석한 모든 사람")
print(partyA.union(partyB))

print("A,B 파티에 모두 참석한 사람")
print(partyA.intersection(partyB))

print("A파티에만 참석한 사람")
print(partyA-partyB)