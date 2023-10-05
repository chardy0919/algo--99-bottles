def bottle_song(num): #link github
	temp = num
	
	while num > 1:
		verse2 = 'bottle' if num == 2 else 'bottles'	

		print(f"{num} bottles of beer on the wall, {num} bottles of beer.")

		print(f"Take one down and pass it around, {num-1} {verse2} of beer on the wall.")

		num-=1

	print(f"1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more,\n{temp} bottles of beer on the wall.")

bottle_song(3)


