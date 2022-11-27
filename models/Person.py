class Char:
    def __init__(self, name, hp, atkyang, atkyin, defyang, defyin, speed, barstrong, barweak, atkelement,
                 races, antirace, power, tower):
        self.name = name
        self.hp = hp
        self.atkyang = atkyang
        self.atkyin = atkyin
        self.defyang = defyang
        self.defyin = defyin
        self.speed = speed
        self.barstrong = barstrong
        self.barweak = barweak
        self.atkelement = atkelement
        self.races = races
        self.antirace = antirace
        self.power = power
        self.tower = tower

    def __repr__(self):
        return f'{self.name}, {self.hp}, {self.atkyang}, {self.atkyin}, {self.defyang}, {self.defyin}, {self.speed}, {self.barstrong}, {self.barweak}, {self.atkelement}, {self.races}, {self.antirace}, {self.power}, {self.tower}'


class Element:
    def __init__(self, sun, moon, fire, water, wood, metal, earth, star):
        self.sun = sun
        self.moon = moon
        self.fire = fire
        self.water = water
        self.wood = wood
        self. metal = metal
        self.earth = earth
        self.star = star

    def __repr__(self):
        return f'{self.sun}, {self.moon}, {self.fire}, {self.water}, {self.wood}, {self.metal}, {self.earth}, {self.star}'


reimu = Char('reimu', 6750, 1170, 1020, 1320, 1260, 1020, ['water', 'star'], ['moon', 'metal'], [8, 0, 0, 0, 0, 0, 0, 0], ['human', 'shrine maiden', 'gensokyo', 'hakurei shrine', 'incident resolver'], ['youkai', 'fairy', 'soul'], 0, [])
marisa = Char('marisa', 5500, 1500, 1350, 1050, 1000, 1020, ['moon', 'metal'], ['sun', 'earth'], [0, 0, 0, 0, 0, 0, 0, 6], ['human', 'magician', 'gensokyo', 'forest of magic', 'star', 'collector', 'incident resolver'], ['fairy', 'beast youkai'], 0, [])
sakuya = Char('sakuya', 4550, 1195, 1105, 925, 916, 1400, ['sun', 'earth'], ['fire', 'star'], [0, 0, 0, 0, 0, 6, 0, 0], ['human', 'maid', 'servant', 'gensokyo', 'scarlet devil mansion', 'incident resolver'], ['vampire'], 0, [])
patchouli = Char('patchouli', 4200, 1000, 1700, 1300, 930, 1250, ['fire', 'water', 'wood', 'metal', 'earth'], ['star'], [4, 4, 3, 3, 3, 3, 3, 0], ['youkai', 'magician', 'mistress', 'gensokyo', 'scarlet devil mansion', 'bibliophile', 'indoor person', 'collector'], [], 0, [])
yukari = Char('yukari', 7850, 930, 840, 1390, 840, 850, ['fire', 'star'], ['moon', 'wood'], [2, 0, 0, 0, 0, 0, 8, 0], ['youkai', 'sage of gensokyo', 'sage', 'mistress', 'greater youkai', 'gensokyo', 'incident resolver'], ['magician', 'shrine maiden'], 0, [])
youmu = Char('youmu', 5050, 1160, 1160, 940, 940, 1240, ['moon', 'earth'], ['sun', 'fire'], [0, 3, 0, 0, 0, 6, 0, 0], ['human', 'phantom', 'soul', 'half-human half-phantom', 'half-youkai', 'servant', 'netherworld', 'hakugyokurou', 'swordswoman', 'incident resolver'], ['soul'], 0, [])
lilly = Char('lilly', 5750, 1150, 750, 1100, 900, 950, ['water', 'star'], ['moon', 'metal'], [0, 0, 0, 0, 6, 0, 0, 2], ['fairy', 'spring', 'gensokyo'], [], 0, [])
reisen = Char('reisen', 5150, 1210, 1080, 1025, 965, 1140, ['sun', 'water'], ['metal', 'star'], [0, 11, 0, 0, 0, 0, 0, 0], ['youkai', 'beast youkai', 'beast', 'rabbit', 'moon rabbit', 'earth rabbit', 'gensokyo', 'bamboo forest of the lost', 'eientei', 'servant', 'moon', 'medicine', 'incident resolver'], ['moon rabbit', 'lunarian'], 0, [])
kasen = Char('kasen', 5850, 1285, 1200, 1045, 1105, 1095, ['earth', 'star'], ['moon', 'fire'], [0, 0, 3, 3, 0, 0, 3, 0], ['hermit', 'youkai', 'oni', 'gensokyo', 'youkai mountain', 'mistress', 'beast', 'sage', 'big four', 'sage of gensokyo', 'martial artist', 'religious'], ['incident resolver', 'soul'], 0, [])
cirno = Char('cirno', 5200, 1120, 1170, 800, 860, 1010, ['moon', 'metal'], ['sun', 'earth'], [0, 0, 0, 12, 0, 0, 0, 0], ['fairy', 'ice', 'cold', 'gensokyo', 'misty lake', 'incident resolver'], [], 0, [])
daiyousei = Char('daiyousei', 4800, 800, 940, 1065, 1095, 1040, ['sun', 'water'], ['metal', 'star'], [0, 0, 2, 0, 2, 6, 0, 0], ['fairy', 'gensokyo', 'flower', 'misty lake', 'incident resolver'], [], 0, [])
alice = Char('alice', 5350, 890, 1080, 910, 1220, 1280, ['sun', 'water'], ['metal', 'star'], [0, 0, 0, 0, 0, 0, 0, 0], ['magician', 'youkai', 'doll', 'gensokyo', 'forest of magic', 'bibliophile', 'collector', 'indoor person', 'demonic person', 'incident resolver'], ['magician'], 0, [])
medicine = Char('medicine', 4650, 990, 1180, 870, 1080, 950, ['water', 'star'], ['moon', 'metal'], [0, 0, 0, 8, 0, 0, 1, 0], ['doll', 'youkai', 'poison', 'medicine', 'flower', 'gensokyo', 'nameless hill'], ['human'], 0, [])
sanae = Char('sanae', 8000, 1000, 940, 985, 945, 980, ['moon', 'water'], ['sun', 'metal'], [0, 0, 0, 2, 2, 4, 4, 3], ['human', 'shrine maiden', 'god', 'living god', 'wind priestess', 'gensokyo', 'youkai mountain', 'moriya shrine', 'incident resolver'], ['aquatic', 'youkai', 'god'], 0, [])
nitori = Char('nitori', 5300, 960, 1120, 950, 1030, 1330, ['sun', 'metal'], ['earth', 'star'], [0, 0, 0, 3, 0, 3, 0, 0], ['youkai', 'kappa', 'aquatic', 'engineer', 'gensokyo', 'youkai mountain', 'genbu ravine'], ['tengu', 'oni'], 0, [])
ran = Char('ran', 5400, 1330, 980, 1180, 890, 990, ['sun', 'earth'], ['fire', 'star'], [0, 0, 0, 0, 0, 0, 4, 0], ['youkai', 'beast youkai', 'beast', 'kitsune', 'shikigami', 'servant', 'mistress', 'gensokyo'], ['youkai', 'fairy', 'human'], 0, [])
chen = Char('chen', 4500, 1220, 880, 985, 815, 1200, ['moon', 'wood'], ['sun', 'water'], [0, 0, 0, 0, 0, 0, 0, 0], ['youkai', 'beast youkai', 'beast', 'cat', 'shikigami', 'servant', 'gensokyo', 'youkai mountain'], ['fairy'], 0, [])
meiling = Char('meiling', 5800, 1190, 1230, 990, 960, 920, ['moon', 'water'], ['sun', 'metal'], [0, 0, 0, 0, 0, 0, 8, 7], ['youkai', 'servant', 'gensokyo', 'scarlet devil mansion'], ['phantom', 'fairy', 'youkai', 'magician', 'human', 'tengu', 'incident resolver', 'beast'], 0, [])
flandre = Char('flandre', 4850, 1180, 1380, 890, 950, 1080, ['moon', 'metal', 'star'], ['sun', 'water', 'wood'], [0, 0, 2, 0, 0, 0, 0, 0], ['youkai', 'devil', 'vampire', 'younger sister', 'magical girl', 'gensokyo', 'scarlet devil mansion', 'indoor person', 'moon'], ['older sister', 'doll'], 0, [])
remilia = Char('remilia', 5000, 1000, 1300, 880, 1050, 1220, ['moon', 'earth', 'star'], ['sun', 'fire', 'metal'], [0, 0, 6, 0, 0, 0, 0, 0], ['youkai', 'devil', 'vampire', 'mistress', 'older sister', 'gensokyo', 'scarlet devil mansion', 'moon', 'incident resolver'], ['younger sister', 'human'], 0, [])
yuyuko = Char('yuyuko', 5350, 1380, 1010, 1280, 990, 1170, ['sun', 'metal'], ['earth', 'star'], [0, 0, 0, 7, 0, 0, 0, 0], ['ghost', 'soul', 'mistress', 'netherworld', 'hakugyokurou', 'collector', 'incident resolver'], [], 0, [])
sunny = Char('sunny', 4350, 1260, 690, 1035, 895, 1250, ['wood', 'star'], ['moon', 'water'], [8, 0, 0, 0, 0, 0, 0, 0], ['fairy', 'sun', 'light', 'gensokyo', 'hakurei shrine', 'three fairies of light', 'incident resolver'], [], 0, [])
luna = Char('luna', 4700, 870, 1220, 960, 1160, 850, ['sun', 'metal'], ['earth', 'star'], [0, 8, 0, 0, 0, 0, 0, 0], ['fairy', 'moon', 'light', 'bibliophile', 'gensokyo', 'hakurei shrine', 'three fairies of light', 'incident resolver'], [], 0, [])
sapphire = Char('star', 5150, 1260, 980, 915, 1035, 780, ['moon', 'water'], ['sun', 'metal'], [0, 0, 0, 0, 0, 0, 0, 8], ['fairy', 'star', 'light', 'gensokyo', 'hakurei shrine', 'three fairies of light', 'incident resolver'], ['human'], 0, [])
mokou = Char('mokou', 5800, 1310, 820, 1050, 1020, 1090, ['wood', 'star'], ['moon', 'water'], [0, 0, 12, 0, 0, 0, 0, 0], ['human', 'person of hourai', 'gensokyo', 'bamboo forest of the lost', 'doll'], ['person of hourai'], 0, [])
seiran = Char('seiran', 4900, 1020, 1110, 980, 1060, 1300, ['sun', 'water'], ['metal', 'star'], [0, 4, 0, 0, 0, 0, 5, 0], ['youkai', 'beast youkai', 'beast rabbit', 'moon rabbit', 'eagle ravi', 'moon'], ['lunar capital'], 0, [])
ringo = Char('ringo', 4900, 980, 1040, 1015, 1095, 1340, ['sun', 'water'], ['metal', 'star'], [0, 6, 0, 0, 0, 0, 2, 0], ['youkai', 'beast youkai', 'beast rabbit', 'moon rabbit', 'eagle ravi', 'moon'], ['lunar capital'], 0, [])
rei_sen = Char('rei_sen', 5300, 680, 870, 1100, 1140, 1150, ['sun', 'water'], ['metal', 'star'], [0, 0, 0, 0, 0, 0, 0, 0], ['youkai', 'beast youkai', 'beast rabbit', 'moon rabbit', 'moon', 'lunar capital', 'servant'], ['gensokyo'], 0, [])
byakuren = Char('byakuren', 7150, 1170, 750, 1130, 1420, 1000, ['wood', 'star'], ['moon', 'water'], [3, 0, 0, 0, 0, 0, 0, 3], ['magician', 'monk', 'superhuman', 'demonic person', 'mistress', 'gensokyo', 'myouren temple', 'martial artist', 'religious'], ['human'], 0, [])
toyohime = Char('toyohime', 6500, 1000, 1500, 950, 1300, 850, ['sun', 'earth'], ['fire', 'star'], [0, 3, 1, 3, 2, 2, 0, 0], ['lunarian', 'moon emissary', 'princess', 'older sister', 'mistress', 'lunar capital', 'moon'], ['youkai', 'gensokyo', 'human'], 0, [])
yorihime = Char('yorihime', 5550, 1000, 1420, 925, 1075, 1370, ['sun', 'water'], ['metal', 'star'], [0, 4, 1, 1, 2, 3, 1, 0], ['lunarian', 'moon emissary', 'princess', 'younger sister', 'mistress', 'lunar capital', 'swordswoman', 'shrine maiden', 'moon', 'god', 'divine spirit'], ['gensokyo', 'human', 'youkai', 'god'], 0, [])
kosuzu = Char('kosuzu', 4900, 980, 1280, 1020, 840, 900, ['moon', 'water'], ['sun', 'metal'], [0, 0, 0, 7, 8, 0, 0, 0], ['human', 'gensokyo', 'human village', 'bibliophile', 'tsukumogami'], ['indoor person', 'poltergeist'], 0, [])
akyuu = Char('akyuu', 4950, 1295, 1155, 915, 815, 830, ['sun', 'water'], ['metal', 'star'], [0, 2, 2, 4, 4, 2, 0, 0], ['human', 'maiden of miare', 'gensokyo', 'human village', 'bibliophile', 'mistress', 'indoor person'], ['oni', 'bibliophile', 'scarlet devil mansion', 'hakugyokurou', 'eientei'], 0, [])
kanako = Char('kanako', 8200, 1170, 990, 1120, 1150, 830, ['earth', 'star'], ['moon', 'fire'], [0, 0, 0, 4, 4, 3, 0, 0], ['god', 'divine spirit', 'gensokyo', 'youkai mountain', 'moriya shrine', 'religious'], ['human', 'aquatic', 'god', 'tengu'], 0, [])
suwako = Char('suwako', 6150, 1200, 1400, 1090, 980, 1000, ['sun', 'fire'], ['wood', 'star'], [0, 0, 0, 4, 4, 2, 4, 0], ['god', 'yaoyorozu no kami', 'gensokyo', 'youkai mountain', 'moriya shrine', 'frog', 'religious'], ['human', 'god', 'tengu', 'kappa', 'shikigami', 'flower'], 0, [])
minoriko = Char('minoriko', 8100, 1100, 1250, 750, 900, 830, ['moon', 'earth'], ['sun', 'fire'], [0, 0, 0, 1, 9, 6, 0, 0], ['divine', 'yaoyorozu no kami', 'autumn', 'younger sister', 'youkai mountain', 'gensokyo', 'religious'], ['oni'], 0, [])
shizuha = Char('shizuha', 5500, 1050, 1300, 1000, 1150, 850, ['sun', 'earth'], ['fire', 'star'], [0, 0, 1, 0, 7, 8, 0, 0], ['divine', 'yaoyorozu no kami', 'autumn', 'older sister', 'youkai mountain', 'gensokyo', 'religious'], ['oni'], 0, [])
koishi = Char('koishi', 6000, 1210, 1390, 1050, 1150, 900, ['fire', 'moon'], ['sun', 'wood'], [0, 0, 0, 9, 3, 0, 0, 0], ['youkai', 'satori', 'underworld', 'former hell', 'palace of the earth spirits', 'gensokyo', 'younger sister'], [], 0, [])
benben = Char('benben', 5500, 1150, 1450, 700, 850, 1200, ['sun', 'water'], ['metal', 'star'], [0, 0, 4, 1, 7, 0, 0, 0], ['tsukumogami', 'yaoyorozu no kami', 'god', 'musician', 'older sister', 'gensokyo'], ['sage', 'mistress'], 0, [])
yatsuhashi = Char('yatsuhashi', 5500, 1450, 1150, 850, 700, 1200, ['moon', 'water'], ['sun', 'metal'], [2, 0, 1, 0, 9, 0, 0, 0], ['tsukumogami', 'yaoyorozu no kami', 'god', 'musician', 'younger sister', 'gensokyo'], ['sage', 'mistress'], 0, [])
koakuma = Char('koakuma', 4500, 1100, 1250, 715, 885, 1150, ['moon', 'star'], ['sun', 'fire'], [0, 3, 9, 2, 0, 2, 0, 0], ['devil', 'servant', 'familiar', 'bibliophile', 'gensokyo', 'scarlet devil mansion', 'youkai'], ['human'], 0, [])
nemuno = Char('nemuno', 5000, 1350, 1500, 750, 950, 900, ['wood', 'moon'], ['sun', 'water'], [0, 0, 3, 0, 4, 9, 0, 0], ['yamanba', 'youkai', 'shrine maiden', 'youkai mountain', 'gensokyo'], ['human'], 0, [])
satori = Char('satori', 6000, 1390, 1210, 1150, 1050, 900, ['moon', 'earth'], ['sun', 'fire'], [0, 0, 9, 0, 0, 0, 3, 0], ['youkai', 'satori', 'underworld', 'former hell', 'palace of the earth spirits', 'gensokyo', 'older sister', 'mistress', 'indoor person', 'bibliophile'], ['beast', 'soul', 'undead'], 0, [])
tewi = Char('tewi', 5150, 1210, 1080, 965, 1025, 1140, ['moon', 'water'], ['sun', 'metal'], [5, 0, 0, 0, 0, 0, 0, 5], ['rabbit', 'beast youkai', 'eientei', 'bamboo forest of the lost', 'gensokyo'], ['human', 'rabbit'], 0, [])
momiji = Char('momiji', 4000, 1010, 1020, 1220, 1400, 1000, ['water', 'star'], ['moon', 'metal'], [0, 0, 0, 0, 10, 0, 0, 0], ['white wolf tengu', 'tengu', 'youkai', 'youkai mountain', 'gensokyo', 'beast', 'swordswoman'], ['beast youkai', 'moon', 'youkai mountain'], 0, [])
hatate = Char('hatate', 5000, 1100, 1200, 950, 900, 1300, ['moon', 'water'], ['sun', 'metal'], [0, 0, 0, 0, 11, 0, 0, 0], ['crow tengu', 'tengu', 'youkai', 'youkai mountain', 'gensokyo', 'indoor person', 'bird'], ['soul', 'kappa', 'tengu'], 0, [])
marisaz1 = Char('marisaz1', 5600, 1500, 1700, 900, 1000, 1130, ['sun', 'moon', 'star'], ['wood'], [3, 0, 5, 2, 0, 0, 3, 9], ['magician', 'youkai', 'gensokyo', 'forest of magic', 'star', 'collector', 'sun', 'parallel presence', 'light', 'scarlet devil mansion'], ['scarlet devil mansion', 'incident resolver'], 0, [])
rumia = Char('rumia', 4900, 670, 1340, 620, 1390, 1000, ['sun', 'metal'], ['earth', 'star'], [3, 6, 0, 3, 2, 0, 0, 0], ['youkai', 'gensokyo', 'dark'], ['light', 'sun', 'hakurei shrine'], 0, [])
hina = Char('hina', 5800, 1300, 1200, 900, 1000, 890, ['sun', 'wood'], ['water', 'star'], [3, 2, 2, 2, 2, 0, 2, 0], ['god', 'unlucky', 'youkai mountain', 'gensokyo', 'youkai', 'doll'], ['god', 'human'], 0, [])
clownpiece = Char('clownpiece', 4800, 840, 1450, 700, 1050, 1000, ['moon', 'wood'], ['sun', 'water'], [4, 6, 4, 2, 1, 0, 0, 4], ['fairy', 'hell', 'hakurei shrine', 'gensokyo', 'incident resolver', 'moon enemy', 'servant'], ['lunar capital', 'lunarian', 'moon rabbit', 'moon'], 0, [])
suika = Char('suika', 6600, 1400, 1520, 910, 970, 780, ['sun', 'earth'], ['fire', 'star'], [0, 3, 4, 2, 1, 3, 0, 0], ['oni', 'youkai', 'youkai mountain', 'gensokyo', 'big Four'], ['human', 'youkai', 'kappa', 'tengu'], 0, [])
aya = Char('aya', 4400, 1200, 1100, 900, 950, 1420, ['sun', 'water'], ['metal', 'star'], [0, 0, 0, 0, 11, 0, 0, 0], ['crow tengu', 'tengu', 'youkai', 'youkai mountain', 'gensokyo'], ['kappa', 'oni'], 0, [])
yoshika = Char('yoshika', 7000, 890, 980, 1090, 1290, 800, ['moon', 'metal'], ['sun', 'earth'], [0, 0, 0, 12, 0, 0, 0, 0], ['jiang shi', 'youkai', 'servant', 'gensokyo', 'undead'], ['soul', 'god'], 0, [])
seiga = Char('seiga', 5550, 1050, 1210, 900, 920, 1260, ['sun', 'metal'], ['earth', 'star'], [0, 0, 1, 6, 1, 0, 4, 6], ['wicked hermit', 'hermit', 'gensokyo', 'divine spirit', 'mausoleum', 'jiang shi', 'mistress'], ['human', 'oni', 'servant', 'hermit', 'shinigami'], 0, [])
sagume = Char('sagume', 5800, 1330, 1140, 1190, 1100, 980, ['sun', 'fire'], ['wood', 'star'], [0, 11, 0, 0, 0, 0, 0, 3], ['lunarian', 'lunar capital', 'moon', 'god', 'divine spirit', 'sage of the moon', 'sage'], ['moon enemy', 'sage', 'incident resolver'], 0, [])
eirin = Char('eirin', 8400, 1500, 1220, 850, 800, 850, ['sun', 'wood'], ['water', 'star'], [0, 7, 0, 0, 1, 0, 0, 0], ['lunarian', 'moon emissary', 'mistress', 'servant', 'person of hourai', 'gensokyo', 'bamboo forest of the lost', 'eientei', 'moon', 'medicine', 'pharmacist', 'sage of the moon', 'sage'], ['moon enemy', 'lunarian', 'moon rabbit'], 0, [])
kaguya = Char('kaguya', 5400, 1480, 1390, 1010, 950, 990, ['sun', 'metal'], ['earth', 'star'], [0, 0, 3, 0, 4, 4, 0, 0], ['lunarian', 'mistress', 'princess', 'person of hourai', 'gensokyo', 'bamboo forest of the lost', 'eientei', 'moon', 'indoor person'], ['lunarian', 'human'], 0, [])
youmur8 = Char('youmur8', 6000, 1600, 1600, 900, 900, 1150, ['fire', 'water', 'wood'], ['earth'], [0, 0, 5, 1, 5, 12, 1, 0], ['human', 'phantom', 'soul', 'half-human half-phantom', 'half-youkai', 'servant', 'netherworld', 'hakugyokurou', 'swordswoman', 'parallel presence', 'flower'], ['fairy', 'soul', 'undead', 'magician', 'swordswoman', 'martial artist'], 0, [])
shion = Char('shion', 6500, 1125, 1575, 900, 1150, 850, ['sun', 'water'], ['metal', 'star'], [0, 0, 12, 0, 0, 0, 0, 0], ['poverty god', 'god', 'unlucky', 'older sister', 'hakurei shrine', 'gensokyo'], ['human', 'youkai', 'older sister', 'younger sister'], 0, [])
aunn = Char('aunn', 4500, 1430, 830, 1330, 930, 1030, ['fire', 'star'], ['moon', 'wood'], [12, 0, 0, 0, 2, 0, 4, 0], ['beast youkai', 'youkai', 'beast', 'divine spirit', 'divine beast', 'statue', 'hakurei shrine', 'moriya shrine', 'myouren temple', 'gensokyo'], ['soul', 'youkai'], 0, [])
kokoro = Char('kokoro', 6075, 1205, 1405, 895, 905, 825, ['moon', 'fire'], ['sun', 'wood'], [0, 0, 0, 0, 0, 0, 12, 4], ['tsukumogami', 'yaoyorozu no kami', 'god', 'noh', 'gensokyo'], ['human', 'god', 'religious'], 0, [])
yuugi = Char('yuugi', 6700, 1320, 1600, 850, 1030, 760, ['moon', 'earth'], ['sun', 'fire'], [0, 0, 0, 0, 1, 6, 5, 6], ['oni', 'youkai', 'underworld', 'former Hell', 'gensokyo', 'big four', 'martial artist'], ['human', 'youkai'], 0, [])
lunasa = Char('lunasa', 7750, 1000, 1450, 700, 850, 900, ['sun', 'water'], ['metal', 'star'], [0, 0, 0, 6, 11, 0, 0, 0], ['Poltergeist', 'Soul', 'gensokyo', 'misty lake', 'musician', 'older sister', 'undead'], ['soul', 'indoor person'], 0, [])
merlin = Char('merlin', 6400, 1450, 1000, 850, 700, 1170, ['earth', 'star'], ['moon', 'fire'], [0, 0, 0, 7, 7, 0, 0, 0], ['Poltergeist', 'Soul', 'gensokyo', 'misty lake', 'musician', 'older sister', 'younger sister', 'undead'], ['soul', 'indoor person'], 0, [])
lyrica = Char('lyrica', 7075, 1225, 1225, 775, 775, 1035, ['moon', 'fire'], ['sun', 'wood'], [0, 0, 0, 5, 8, 0, 0, 0], ['Poltergeist', 'Soul', 'gensokyo', 'misty lake', 'musician', 'older sister', 'younger sister', 'undead'], ['soul', 'indoor person'], 0, [])
