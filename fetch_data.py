#usr/bin/python27 -tt

import urllib
import re

"""Script fetches data on tennis grand slam champions 2003-2013."""

def fetch_file():
	"""Fetches and returns cleaned-up data from Wikipedia."""
	f = urllib.urlopen("https://en.wikipedia.org/wiki/List_of_Grand_Slam_men's_singles_champions")
	text = f.read()
	beginning = re.search(r"<tr>\s*<td>\s*<b>\s*2003", text).regs[0][0]
	end = re.search(r"<tr>\s*<td>\s*<b>\s*2014", text).regs[0][0]
	text = text[beginning:end]
	text = re.sub(r"<small>\(\d+/\d+\)</small>", "", text)
	text = re.sub(r'<span class="flagicon">.+</span>', "", text)
	text = re.sub(r'<a href=".+?" title=".+?">', "", text)
	text = re.sub(r'</a>', "", text)
	text = re.sub(r"[ABCDEFGHIJKLMNOPQRSTUVWXYZ]+:", "", text)
	text = re.sub(r' style="background:.+?[;]*"', "", text)
	text = re.sub(r"<[/]*b>", "", text)
	return text


def sort_data():
	"""Sorts the data and returns a hash table with each champion's name as the key."""
	text = fetch_file()
	tours = text.split("<tr>")[1:]
	
	wimbledon = []
	french = []
	aus = []
	usa = []
	years = []
	champions = {}

	for tour in tours:
		matches = re.findall("<td>(.+?)</td>", tour)
		years.append(matches[0].strip())
		aus.append(matches[1].strip())
		french.append(matches[2].strip())
		wimbledon.append(matches[3].strip())
		usa.append(matches[4].strip())
	
	for i in range(len(years)):
		if aus[i] in champions.keys():
			champions[aus[i]].append(years[i])
		else:
			champions[aus[i]] = [years[i]]

		if french[i] in champions.keys():
			champions[french[i]].append(years[i])
		else:
			champions[french[i]] = [years[i]]

		if wimbledon[i] in champions.keys():
			champions[wimbledon[i]].append(years[i])
		else:
			champions[wimbledon[i]] = [years[i]]

		if usa[i] in champions.keys():
			champions[usa[i]].append(years[i])
		else:
			champions[usa[i]] = [years[i]]
	
	return champions


def write_to_file(filename):
	"""Writes data on Grand Slam Champions to the file with the name entered in the 'filename' parameter."""
	champions = sort_data()
	f = open(filename, "w")

	for champ in champions.keys():
		f.write(champ + ": ")
		for year in champions[champ]:
			f.write(year + ", ")
		f.write("\n")
	
	f.close()


def main():
	"""Calls write_to_file function to write the data obtained to the filename variable."""
	filename = "data.txt"
	write_to_file(filename)


if __name__ == "__main__":
	main()
