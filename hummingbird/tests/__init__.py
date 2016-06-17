#!/usr/bin/env python

""" Tests split by class. """

import unittest
import hummingbird


class HummingbirdTest(unittest.TestCase, object):
    def setUp(self):
        self.un = 'HummingbirdpyTest'
        # Security through obscurity. Do you really want to get into my test
        # Account?
        self.un_pswd = str(8) * 8
        self.api = hummingbird.Hummingbird(self.un, self.un_pswd)

    def test_get_anime_function(self):
        """ Test if fetching an anime object works """
        anime = self.api.get_anime('neon-genesis-evangelion')
        self.assertEqual(anime.title, 'Neon Genesis Evangelion')

    def test_title_language_get_anime_function(self):
        """ Test if setting the prefered language works """
        anime = self.api.get_anime('neon-genesis-evangelion',
                                   title_language='romanized')
        self.assertEqual(anime.title, 'Shinseiki Evangelion')

    def test_search_anime_function(self):
        """ Test if searching for anime works well. """
        search = self.api.search_anime('evangelion')
        for item in search:
            self.assertIn(item.title, ['Petit Eva: Evangelion@School',
                                       'Neon Genesis Evangelion',
                                       'Neon Genesis Evangelion: The End of Evangelion',
                                       'Evangelion: 1.0 You Are (Not) Alone',
                                       'Evangelion: 2.0 You Can (Not) Advance',
                                       'Evangelion: 3.0 You Can (Not) Redo ',
                                       'Neon Genesis Evangelion: Death & Rebirth',
                                       'Schick x Evangelion',
                                       'Evangelion x JRA',
                                       'Evangelion: 3.0+1.0'])

    def test_get_library(self):
        """ Test if getting a users library works """
        library = self.api.get_library(self.un)
        for item in library:
            print(item.anime.title)

    def test_get_user(self):
        """ Test if getting user info works """
        user = self.api.get_user('covabishop')  # Shameless self-promotion
        print(user.waifu)

    def test_get_feed(self):
        """ Tests getting user feed """
        feed = self.api.get_feed(self.un)
        for item in feed:
            print(item.story_id)

    def test_get_favorites(self):
        """ Tests getting user favorites. """
        favs = self.api.get_favorites('covabishop')
        for fav in favs:
            current = self.api.get_anime(fav.anime_id)
            print(current.title)

if __name__ == '__main__':
        unittest.main()
