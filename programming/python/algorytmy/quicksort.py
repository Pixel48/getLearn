def quickSort(arr):
  if len(arr) < 2: return arr
  pivot = arr.pop()
  top = []
  bot = []
  for char in arr:
    if char > pivot: top.append(char)
    else: bot.append(char)
  return quickSort(bot) + [pivot] + quickSort(top)
