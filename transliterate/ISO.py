# (C) 2021 எழில் மொழி அறக்கட்டளை
# இந்த நிரல் ஓப்பன்-தமிழ் திரட்டின் ஒரு பகுதி.
# தமிழ் மொழி ஒலிவழி எழுத்துவடிவமைப்பு சென்னை பல்கலைக்கழகத்தின் தரபத்தில் வருவது.
# மேலும் காண்க: https://en.wikipedia.org/wiki/ISO_15919

import copy
from collections import OrderedDict

from tamil.utf8 import grantha_mei_letters
from tamil.utf8 import uyir_letters, grantha_agaram_letters, aytham_letter

uyir_letters_plus_aytham = copy.deepcopy(uyir_letters)
uyir_letters_plus_aytham.extend(aytham_letter)

transliterate_uyir_plus_aytham = ["a","ā","i","ī","u","ū","e","ē","ai","o","ō","au","ḵ"]
transliterate_all_mei_agaram = ["k","c","ṭ","t","p","ṟ","ñ","ṅ","ṇ","ṉ","m","ṉ","y","r","l","v","ḻ","ḷ","ś","j","ṣ","s","h","s̤"]
transliterate_all_mei = transliterate_all_mei_agaram ##["i"+code for code in transliterate_all_mei_agaram]

UYIR_MAP = dict(zip(uyir_letters_plus_aytham,transliterate_uyir_plus_aytham))
AGARAM_MAP = dict(zip(grantha_agaram_letters,transliterate_all_mei_agaram))
MEI_MAP = dict(zip(grantha_agaram_letters,transliterate_all_mei))

class Transliteration:
    table = OrderedDict()
    table.update(zip(transliterate_uyir_plus_aytham,uyir_letters_plus_aytham))
    table.update(zip(transliterate_all_mei,grantha_mei_letters))
    table[u'n'] = u'ந்'
    table[u'ka'] = u'க'
    table[u'kā'] = u'கா'
    table[u'ki'] = u'கி'
    table[u'kī'] = u'கீ'
    table[u'ku'] = u'கு'
    table[u'kū'] = u'கூ'
    table[u'ke'] = u'கெ'
    table[u'kē'] = u'கே'
    table[u'kai'] = u'கை'
    table[u'ko'] = u'கொ'
    table[u'kō'] = u'கோ'
    table[u'kau'] = u'கௌ'
    table[u'ca'] = u'ச'
    table[u'cā'] = u'சா'
    table[u'ci'] = u'சி'
    table[u'cī'] = u'சீ'
    table[u'cu'] = u'சு'
    table[u'cū'] = u'சூ'
    table[u'ce'] = u'செ'
    table[u'cē'] = u'சே'
    table[u'cai'] = u'சை'
    table[u'co'] = u'சொ'
    table[u'cō'] = u'சோ'
    table[u'cau'] = u'சௌ'
    table[u'ṭa'] = u'ட'
    table[u'ṭā'] = u'டா'
    table[u'ṭi'] = u'டி'
    table[u'ṭī'] = u'டீ'
    table[u'ṭu'] = u'டு'
    table[u'ṭū'] = u'டூ'
    table[u'ṭe'] = u'டெ'
    table[u'ṭē'] = u'டே'
    table[u'ṭai'] = u'டை'
    table[u'ṭo'] = u'டொ'
    table[u'ṭō'] = u'டோ'
    table[u'ṭau'] = u'டௌ'
    table[u'ta'] = u'த'
    table[u'tā'] = u'தா'
    table[u'ti'] = u'தி'
    table[u'tī'] = u'தீ'
    table[u'tu'] = u'து'
    table[u'tū'] = u'தூ'
    table[u'te'] = u'தெ'
    table[u'tē'] = u'தே'
    table[u'tai'] = u'தை'
    table[u'to'] = u'தொ'
    table[u'tō'] = u'தோ'
    table[u'tau'] = u'தௌ'
    table[u'pa'] = u'ப'
    table[u'pā'] = u'பா'
    table[u'pi'] = u'பி'
    table[u'pī'] = u'பீ'
    table[u'pu'] = u'பு'
    table[u'pū'] = u'பூ'
    table[u'pe'] = u'பெ'
    table[u'pē'] = u'பே'
    table[u'pai'] = u'பை'
    table[u'po'] = u'பொ'
    table[u'pō'] = u'போ'
    table[u'pau'] = u'பௌ'
    table[u'ṟa'] = u'ற'
    table[u'ṟā'] = u'றா'
    table[u'ṟi'] = u'றி'
    table[u'ṟī'] = u'றீ'
    table[u'ṟu'] = u'று'
    table[u'ṟū'] = u'றூ'
    table[u'ṟe'] = u'றெ'
    table[u'ṟē'] = u'றே'
    table[u'ṟai'] = u'றை'
    table[u'ṟo'] = u'றொ'
    table[u'ṟō'] = u'றோ'
    table[u'ṟau'] = u'றௌ'
    table[u'ña'] = u'ஞ'
    table[u'ñā'] = u'ஞா'
    table[u'ñi'] = u'ஞி'
    table[u'ñī'] = u'ஞீ'
    table[u'ñu'] = u'ஞு'
    table[u'ñū'] = u'ஞூ'
    table[u'ñe'] = u'ஞெ'
    table[u'ñē'] = u'ஞே'
    table[u'ñai'] = u'ஞை'
    table[u'ño'] = u'ஞொ'
    table[u'ñō'] = u'ஞோ'
    table[u'ñau'] = u'ஞௌ'
    table[u'ṅa'] = u'ங'
    table[u'ṅā'] = u'ஙா'
    table[u'ṅi'] = u'ஙி'
    table[u'ṅī'] = u'ஙீ'
    table[u'ṅu'] = u'ஙு'
    table[u'ṅū'] = u'ஙூ'
    table[u'ṅe'] = u'ஙெ'
    table[u'ṅē'] = u'ஙே'
    table[u'ṅai'] = u'ஙை'
    table[u'ṅo'] = u'ஙொ'
    table[u'ṅō'] = u'ஙோ'
    table[u'ṅau'] = u'ஙௌ'
    table[u'ṇa'] = u'ண'
    table[u'ṇā'] = u'ணா'
    table[u'ṇi'] = u'ணி'
    table[u'ṇī'] = u'ணீ'
    table[u'ṇu'] = u'ணு'
    table[u'ṇū'] = u'ணூ'
    table[u'ṇe'] = u'ணெ'
    table[u'ṇē'] = u'ணே'
    table[u'ṇai'] = u'ணை'
    table[u'ṇo'] = u'ணொ'
    table[u'ṇō'] = u'ணோ'
    table[u'ṇau'] = u'ணௌ'
    table[u'na'] = u'ந'
    table[u'nā'] = u'நா'
    table[u'ni'] = u'நி'
    table[u'nī'] = u'நீ'
    table[u'nu'] = u'நு'
    table[u'nū'] = u'நூ'
    table[u'ne'] = u'நெ'
    table[u'nē'] = u'நே'
    table[u'nai'] = u'நை'
    table[u'no'] = u'நொ'
    table[u'nō'] = u'நோ'
    table[u'nau'] = u'நௌ'
    table[u'ma'] = u'ம'
    table[u'mā'] = u'மா'
    table[u'mi'] = u'மி'
    table[u'mī'] = u'மீ'
    table[u'mu'] = u'மு'
    table[u'mū'] = u'மூ'
    table[u'me'] = u'மெ'
    table[u'mē'] = u'மே'
    table[u'mai'] = u'மை'
    table[u'mo'] = u'மொ'
    table[u'mō'] = u'மோ'
    table[u'mau'] = u'மௌ'
    table[u'ṉa'] = u'ன'
    table[u'ṉā'] = u'னா'
    table[u'ṉi'] = u'னி'
    table[u'ṉī'] = u'னீ'
    table[u'ṉu'] = u'னு'
    table[u'ṉū'] = u'னூ'
    table[u'ṉe'] = u'னெ'
    table[u'ṉē'] = u'னே'
    table[u'ṉai'] = u'னை'
    table[u'ṉo'] = u'னொ'
    table[u'ṉō'] = u'னோ'
    table[u'ṉau'] = u'னௌ'
    table[u'ya'] = u'ய'
    table[u'yā'] = u'யா'
    table[u'yi'] = u'யி'
    table[u'yī'] = u'யீ'
    table[u'yu'] = u'யு'
    table[u'yū'] = u'யூ'
    table[u'ye'] = u'யெ'
    table[u'yē'] = u'யே'
    table[u'yai'] = u'யை'
    table[u'yo'] = u'யொ'
    table[u'yō'] = u'யோ'
    table[u'yau'] = u'யௌ'
    table[u'ra'] = u'ர'
    table[u'rā'] = u'ரா'
    table[u'ri'] = u'ரி'
    table[u'rī'] = u'ரீ'
    table[u'ru'] = u'ரு'
    table[u'rū'] = u'ரூ'
    table[u're'] = u'ரெ'
    table[u'rē'] = u'ரே'
    table[u'rai'] = u'ரை'
    table[u'ro'] = u'ரொ'
    table[u'rō'] = u'ரோ'
    table[u'rau'] = u'ரௌ'
    table[u'la'] = u'ல'
    table[u'lā'] = u'லா'
    table[u'li'] = u'லி'
    table[u'lī'] = u'லீ'
    table[u'lu'] = u'லு'
    table[u'lū'] = u'லூ'
    table[u'le'] = u'லெ'
    table[u'lē'] = u'லே'
    table[u'lai'] = u'லை'
    table[u'lo'] = u'லொ'
    table[u'lō'] = u'லோ'
    table[u'lau'] = u'லௌ'
    table[u'va'] = u'வ'
    table[u'vā'] = u'வா'
    table[u'vi'] = u'வி'
    table[u'vī'] = u'வீ'
    table[u'vu'] = u'வு'
    table[u'vū'] = u'வூ'
    table[u've'] = u'வெ'
    table[u'vē'] = u'வே'
    table[u'vai'] = u'வை'
    table[u'vo'] = u'வொ'
    table[u'vō'] = u'வோ'
    table[u'vau'] = u'வௌ'
    table[u'ḻa'] = u'ழ'
    table[u'ḻā'] = u'ழா'
    table[u'ḻi'] = u'ழி'
    table[u'ḻī'] = u'ழீ'
    table[u'ḻu'] = u'ழு'
    table[u'ḻū'] = u'ழூ'
    table[u'ḻe'] = u'ழெ'
    table[u'ḻē'] = u'ழே'
    table[u'ḻai'] = u'ழை'
    table[u'ḻo'] = u'ழொ'
    table[u'ḻō'] = u'ழோ'
    table[u'ḻau'] = u'ழௌ'
    table[u'ḷa'] = u'ள'
    table[u'ḷā'] = u'ளா'
    table[u'ḷi'] = u'ளி'
    table[u'ḷī'] = u'ளீ'
    table[u'ḷu'] = u'ளு'
    table[u'ḷū'] = u'ளூ'
    table[u'ḷe'] = u'ளெ'
    table[u'ḷē'] = u'ளே'
    table[u'ḷai'] = u'ளை'
    table[u'ḷo'] = u'ளொ'
    table[u'ḷō'] = u'ளோ'
    table[u'ḷau'] = u'ளௌ'
    table[u'śa'] = u'ஶ'
    table[u'ja'] = u'ஜ'
    table[u'ṣa'] = u'ஷ'
    table[u'sa'] = u'ஸ'
    table[u'ha'] = u'ஹ'
    table[u's̤a'] = u'க்ஷ'

class ReverseTransliteration:
    table = OrderedDict()
    table[u'அ'] = u'a'
    table[u'ஆ'] = u'ā'
    table[u'இ'] = u'i'
    table[u'ஈ'] = u'ī'
    table[u'உ'] = u'u'
    table[u'ஊ'] = u'ū'
    table[u'எ'] = u'e'
    table[u'ஏ'] = u'ē'
    table[u'ஐ'] = u'ai'
    table[u'ஒ'] = u'o'
    table[u'ஓ'] = u'ō'
    table[u'ஔ'] = u'au'
    table[u'ஃ'] = u'ḵ'
    table[u'க்'] = u'k'
    table[u'ச்'] = u'c'
    table[u'ட்'] = u'ṭ'
    table[u'த்'] = u't'
    table[u'ப்'] = u'p'
    table[u'ற்'] = u'ṟ'
    table[u'ஞ்'] = u'ñ'
    table[u'ங்'] = u'ṅ'
    table[u'ண்'] = u'ṇ'
    table[u'ன்'] = u'ṉ'
    table[u'ந்'] = u'n'
    table[u'ம்'] = u'm'
    table[u'ய்'] = u'y'
    table[u'ர்'] = u'r'
    table[u'ல்'] = u'l'
    table[u'வ்'] = u'v'
    table[u'ழ்'] = u'ḻ'
    table[u'ள்'] = u'ḷ'
    table[u'ஶ்'] = u'ś'
    table[u'ஜ்'] = u'j'
    table[u'ஷ்'] = u'ṣ'
    table[u'ஸ்'] = u's'
    table[u'ஹ்'] = u'h'
    table[u'க்ஷ்'] = u's̤'
    table[u'ஶ'] = u'ś'
    table[u'ஜ'] = u'ja'
    table[u'ஷ'] = u'ṣa'
    table[u'ஸ'] = u'sa'
    table[u'ஹ'] = u'ha'
    table[u'க்ஷ'] = u's̤a'
    table[u'க'] = u'ka'
    table[u'கா'] = u'kā'
    table[u'கி'] = u'ki'
    table[u'கீ'] = u'kī'
    table[u'கு'] = u'ku'
    table[u'கூ'] = u'kū'
    table[u'கெ'] = u'ke'
    table[u'கே'] = u'kē'
    table[u'கை'] = u'kai'
    table[u'கொ'] = u'ko'
    table[u'கோ'] = u'kō'
    table[u'கௌ'] = u'kau'
    table[u'ச'] = u'ca'
    table[u'சா'] = u'cā'
    table[u'சி'] = u'ci'
    table[u'சீ'] = u'cī'
    table[u'சு'] = u'cu'
    table[u'சூ'] = u'cū'
    table[u'செ'] = u'ce'
    table[u'சே'] = u'cē'
    table[u'சை'] = u'cai'
    table[u'சொ'] = u'co'
    table[u'சோ'] = u'cō'
    table[u'சௌ'] = u'cau'
    table[u'ட'] = u'ṭa'
    table[u'டா'] = u'ṭā'
    table[u'டி'] = u'ṭi'
    table[u'டீ'] = u'ṭī'
    table[u'டு'] = u'ṭu'
    table[u'டூ'] = u'ṭū'
    table[u'டெ'] = u'ṭe'
    table[u'டே'] = u'ṭē'
    table[u'டை'] = u'ṭai'
    table[u'டொ'] = u'ṭo'
    table[u'டோ'] = u'ṭō'
    table[u'டௌ'] = u'ṭau'
    table[u'த'] = u'ta'
    table[u'தா'] = u'tā'
    table[u'தி'] = u'ti'
    table[u'தீ'] = u'tī'
    table[u'து'] = u'tu'
    table[u'தூ'] = u'tū'
    table[u'தெ'] = u'te'
    table[u'தே'] = u'tē'
    table[u'தை'] = u'tai'
    table[u'தொ'] = u'to'
    table[u'தோ'] = u'tō'
    table[u'தௌ'] = u'tau'
    table[u'ப'] = u'pa'
    table[u'பா'] = u'pā'
    table[u'பி'] = u'pi'
    table[u'பீ'] = u'pī'
    table[u'பு'] = u'pu'
    table[u'பூ'] = u'pū'
    table[u'பெ'] = u'pe'
    table[u'பே'] = u'pē'
    table[u'பை'] = u'pai'
    table[u'பொ'] = u'po'
    table[u'போ'] = u'pō'
    table[u'பௌ'] = u'pau'
    table[u'ற'] = u'ṟa'
    table[u'றா'] = u'ṟā'
    table[u'றி'] = u'ṟi'
    table[u'றீ'] = u'ṟī'
    table[u'று'] = u'ṟu'
    table[u'றூ'] = u'ṟū'
    table[u'றெ'] = u'ṟe'
    table[u'றே'] = u'ṟē'
    table[u'றை'] = u'ṟai'
    table[u'றொ'] = u'ṟo'
    table[u'றோ'] = u'ṟō'
    table[u'றௌ'] = u'ṟau'
    table[u'ஞ'] = u'ña'
    table[u'ஞா'] = u'ñā'
    table[u'ஞி'] = u'ñi'
    table[u'ஞீ'] = u'ñī'
    table[u'ஞு'] = u'ñu'
    table[u'ஞூ'] = u'ñū'
    table[u'ஞெ'] = u'ñe'
    table[u'ஞே'] = u'ñē'
    table[u'ஞை'] = u'ñai'
    table[u'ஞொ'] = u'ño'
    table[u'ஞோ'] = u'ñō'
    table[u'ஞௌ'] = u'ñau'
    table[u'ங'] = u'ṅa'
    table[u'ஙா'] = u'ṅā'
    table[u'ஙி'] = u'ṅi'
    table[u'ஙீ'] = u'ṅī'
    table[u'ஙு'] = u'ṅu'
    table[u'ஙூ'] = u'ṅū'
    table[u'ஙெ'] = u'ṅe'
    table[u'ஙே'] = u'ṅē'
    table[u'ஙை'] = u'ṅai'
    table[u'ஙொ'] = u'ṅo'
    table[u'ஙோ'] = u'ṅō'
    table[u'ஙௌ'] = u'ṅau'
    table[u'ண'] = u'ṇa'
    table[u'ணா'] = u'ṇā'
    table[u'ணி'] = u'ṇi'
    table[u'ணீ'] = u'ṇī'
    table[u'ணு'] = u'ṇu'
    table[u'ணூ'] = u'ṇū'
    table[u'ணெ'] = u'ṇe'
    table[u'ணே'] = u'ṇē'
    table[u'ணை'] = u'ṇai'
    table[u'ணொ'] = u'ṇo'
    table[u'ணோ'] = u'ṇō'
    table[u'ணௌ'] = u'ṇau'
    table[u'ந'] = u'na'
    table[u'நா'] = u'nā'
    table[u'நி'] = u'ni'
    table[u'நீ'] = u'nī'
    table[u'நு'] = u'nu'
    table[u'நூ'] = u'nū'
    table[u'நெ'] = u'ne'
    table[u'நே'] = u'nē'
    table[u'நை'] = u'nai'
    table[u'நொ'] = u'no'
    table[u'நோ'] = u'nō'
    table[u'நௌ'] = u'nau'
    table[u'ம'] = u'ma'
    table[u'மா'] = u'mā'
    table[u'மி'] = u'mi'
    table[u'மீ'] = u'mī'
    table[u'மு'] = u'mu'
    table[u'மூ'] = u'mū'
    table[u'மெ'] = u'me'
    table[u'மே'] = u'mē'
    table[u'மை'] = u'mai'
    table[u'மொ'] = u'mo'
    table[u'மோ'] = u'mō'
    table[u'மௌ'] = u'mau'
    table[u'ன'] = u'ṉa'
    table[u'னா'] = u'ṉā'
    table[u'னி'] = u'ṉi'
    table[u'னீ'] = u'ṉī'
    table[u'னு'] = u'ṉu'
    table[u'னூ'] = u'ṉū'
    table[u'னெ'] = u'ṉe'
    table[u'னே'] = u'ṉē'
    table[u'னை'] = u'ṉai'
    table[u'னொ'] = u'ṉo'
    table[u'னோ'] = u'ṉō'
    table[u'னௌ'] = u'ṉau'
    table[u'ய'] = u'ya'
    table[u'யா'] = u'yā'
    table[u'யி'] = u'yi'
    table[u'யீ'] = u'yī'
    table[u'யு'] = u'yu'
    table[u'யூ'] = u'yū'
    table[u'யெ'] = u'ye'
    table[u'யே'] = u'yē'
    table[u'யை'] = u'yai'
    table[u'யொ'] = u'yo'
    table[u'யோ'] = u'yō'
    table[u'யௌ'] = u'yau'
    table[u'ர'] = u'ra'
    table[u'ரா'] = u'rā'
    table[u'ரி'] = u'ri'
    table[u'ரீ'] = u'rī'
    table[u'ரு'] = u'ru'
    table[u'ரூ'] = u'rū'
    table[u'ரெ'] = u're'
    table[u'ரே'] = u'rē'
    table[u'ரை'] = u'rai'
    table[u'ரொ'] = u'ro'
    table[u'ரோ'] = u'rō'
    table[u'ரௌ'] = u'rau'
    table[u'ல'] = u'la'
    table[u'லா'] = u'lā'
    table[u'லி'] = u'li'
    table[u'லீ'] = u'lī'
    table[u'லு'] = u'lu'
    table[u'லூ'] = u'lū'
    table[u'லெ'] = u'le'
    table[u'லே'] = u'lē'
    table[u'லை'] = u'lai'
    table[u'லொ'] = u'lo'
    table[u'லோ'] = u'lō'
    table[u'லௌ'] = u'lau'
    table[u'வ'] = u'va'
    table[u'வா'] = u'vā'
    table[u'வி'] = u'vi'
    table[u'வீ'] = u'vī'
    table[u'வு'] = u'vu'
    table[u'வூ'] = u'vū'
    table[u'வெ'] = u've'
    table[u'வே'] = u'vē'
    table[u'வை'] = u'vai'
    table[u'வொ'] = u'vo'
    table[u'வோ'] = u'vō'
    table[u'வௌ'] = u'vau'
    table[u'ழ'] = u'ḻa'
    table[u'ழா'] = u'ḻā'
    table[u'ழி'] = u'ḻi'
    table[u'ழீ'] = u'ḻī'
    table[u'ழு'] = u'ḻu'
    table[u'ழூ'] = u'ḻū'
    table[u'ழெ'] = u'ḻe'
    table[u'ழே'] = u'ḻē'
    table[u'ழை'] = u'ḻai'
    table[u'ழொ'] = u'ḻo'
    table[u'ழோ'] = u'ḻō'
    table[u'ழௌ'] = u'ḻau'
    table[u'ள'] = u'ḷa'
    table[u'ளா'] = u'ḷā'
    table[u'ளி'] = u'ḷi'
    table[u'ளீ'] = u'ḷī'
    table[u'ளு'] = u'ḷu'
    table[u'ளூ'] = u'ḷū'
    table[u'ளெ'] = u'ḷe'
    table[u'ளே'] = u'ḷē'
    table[u'ளை'] = u'ḷai'
    table[u'ளொ'] = u'ḷo'
    table[u'ளோ'] = u'ḷō'
    table[u'ளௌ'] = u'ḷau'

if __name__ == u"__main__":
    from tamil import utf8
#    for l in utf8.uyirmei_letters:
#        mei,uyir = utf8.splitMeiUyir(l)
#        agaram = utf8.mei_to_agaram(mei)
#        print(u"    table[u'%s'] = u'%s'"%(l,AGARAM_MAP[agaram]+UYIR_MAP[uyir]))
    for k,v in Transliteration.table.items():
        print(u"    table[u'%s'] = u'%s'"%(v,k))
