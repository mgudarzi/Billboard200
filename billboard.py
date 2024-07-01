from bs4 import BeautifulSoup
import os
import unittest


def get_soup(file):
    """returns a soup object from the passed file"""

    # get the path to the currently executing file
    dir = os.path.dirname(__file__)

    # open a file handle object on that file
    fileh = open(os.path.join(dir, file))

    # read the contents of the file as a string
    page = fileh.read()

    # close the file handle object
    fileh.close()

    # create a soup object from the HTML string data
    soup = BeautifulSoup(page, "html.parser")

    # return the soup object
    return soup


def get_peak_at_1(soup):
    """Return a list of song titles where the songs peaked at number 1"""

    # declare variables
    title_list = []
    peak_list = []
    out_list = []

    # get the song titles
    title_tags = soup.find_all("span", class_="chart-element__information__song")
    for song_tag in title_tags:
        title_list.append(song_tag.text)

    # get the positions last week
    peak_tags = soup.find_all(
        class_="chart-element__meta text--center color--secondary text--peak"
    )
    for pos_tag in peak_tags:
        peak = pos_tag.text
        peak_list.append(int(peak))

    # create the output list
    for i in range(len(title_list)):
        peak = peak_list[i]
        if peak == 1:
            out_list.append(title_list[i])

    # return the output list
    return out_list


def get_top_5_pos_change(soup):
    """Return a list of tuples (title, change) for the top 5 songs with the highest positive change."""
    out_tup_list = []

    title_tags = soup.find_all("span", class_="chart-element__information__song")
    current_ranks = soup.find_all("span", class_="chart-element__rank__number")
    last_week_ranks = soup.find_all(
        class_="chart-element__meta text--center color--secondary text--last"
    )

    for title_tag, current_rank, last_week_rank in zip(
        title_tags, current_ranks, last_week_ranks
    ):
        title = title_tag.text
        current = int(current_rank.text)
        last = 201 if last_week_rank.text == "-" else int(last_week_rank.text)
        change = last - current
        if change > 0:
            out_tup_list.append((title, change))

    out_tup_list = sorted(out_tup_list, key=lambda x: x[1], reverse=True)[:5]

    return out_tup_list


def get_songs_gt_weeks(soup, num_weeks):
    """Return a list of song titles where the song has been on the chart
    for more than the passed num_weeks"""
    out_list = []

    title_tags = soup.find_all("span", class_="chart-element__information__song")
    chart_tags = soup.find_all(
        "span", class_="chart-element__meta text--center color--secondary text--week"
    )

    for song_tag, week_tag in zip(title_tags, chart_tags):
        song = song_tag.text
        week = int(week_tag.text)
        if week > num_weeks:
            out_list.append(song)

    return out_list


def main():
    file = "BillboardGlobal200-2021.html"
    soup = get_soup(file)
    list = get_top_5_pos_change(soup)
    print(list)
    list = get_peak_at_1(soup)
    list = get_songs_gt_weeks(soup, 40)
    # print(list)


class TestAllMethods(unittest.TestCase):

    def setUp(self):
        file = "BillboardGlobal200-2021.html"
        self.soup = get_soup(file)

    def test_get_top_5_pos_change(self):
        self.assertEqual(
            get_top_5_pos_change(self.soup),
            [
                ("Having Our Way", 184),
                ("Solar Power", 175),
                ("THOT SHIT", 174),
                ("Need To Know", 172),
                ("No Return", 163),
            ],
        )

    def test_get_peak_at_1(self):
        self.assertEqual(
            get_peak_at_1(self.soup),
            [
                "Good 4 U",
                "Butter",
                "Save Your Tears",
                "Montero (Call Me By Your Name)",
                "Peaches",
                "Drivers License",
                "Dynamite",
                "Dakiti",
                "Savage Love (Laxed - Siren Beat)",
                "Positions",
                "WAP",
            ],
        )

    def test_get_songs_gt_weeks(self):
        out = sorted(get_songs_gt_weeks(self.soup, 40))
        self.assertEqual(len(out), 35)
        self.assertEqual(out[0], "Bad Guy")
        self.assertEqual(out[-1], "You Broke Me First.")
        out = get_songs_gt_weeks(self.soup, 41)
        self.assertEqual(len(out), 0)


if __name__ == "__main__":
    # main()
    unittest.main(verbosity=2)
