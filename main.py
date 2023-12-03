
def count_batteries_by_health(present_capacities):
  count = {"healthy": 0, "exchange": 0, "failed": 0}
  for present_capacity in present_capacities:
    rated_cap=120
    soh=(present_capacity / ratedcap)*100
    if soh>80:
      count["healthy"]+=1
    elif 62 <=soh<=80:
      count["exchange"]+=1
    else :
      count["failed"]+=1
  return count
  
      
  


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
