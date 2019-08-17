import sys, json
import re


class Rule:
  def _compile_cat (self, cat):
    cat = re.sub(r'\?', '(?:_LIGHT|_SUBJ)', cat)
    return r'^' + cat + '$'

  def __init__(self, cats=()):
    self.categories = []
    for cat in cats:
      self.categories.append(self._compile_cat(cat))
      self.matched = []

  def match(self, cats):
    self.matched = []
    for cat in cats:
      for regexp in self.categories:
        if re.match(regexp, cat):
          self.matched.append(cat)
    if self.matched:
      return self.matched
    else:
      return []


class Scl:
  def __init__(self):
      self.rules = {
        'sex': Rule(cats=(
             "/?/Health/Med/Sexual/AIDS",
             "/?/Health/Med/Sexual/BreastHealth",
             "/?/Health/Med/Sexual/Contraception",
             "/?/Health/Med/Sexual/Obstetrics",
             "/?/Health/Med/Sexual/Sexology",
             "/?/Health/Med/Sexual/Urology",
             "/?/Health/Med/Sexual/Venereology",
             "/?/Health/Beauty/Cosmetology/BreastBeauty"    
        )),
        'porno': Rule(cats=(
            "/?/Leisure/PersonalLife/Adult/EroPorno",
            "/?/Accidents/Criminal/SexCrime/Pedophilia/ChildPornography"
        )),
        'adult': Rule(cats=(
            "/?/Leisure/PersonalLife/Adult/AboutSex",
             "/?/Leisure/PersonalLife/Adult/BDSM",
             "/?/Leisure/PersonalLife/Adult/IntimateService",
             "/?/Leisure/PersonalLife/Adult/LGBT",
             "/?/Leisure/PersonalLife/Adult/Loli",
             "/?/Leisure/PersonalLife/Adult/Nudism",
             "/?/Leisure/PersonalLife/Adult/SexShops",
             "/?/Leisure/PersonalLife/Adult/VirtualSex",
             "/?/Leisure/PersonalLife/Adult/Swinging",
             "/?/Accidents/Criminal/SexCrime/Rape",
             "/?/Accidents/Criminal/SexCrime/Harassment",
             "/?/Accidents/Criminal/SexCrime/SexualExploitation",
             "/?/Accidents/Criminal/SexCrime/Pedophilia",
             "/?/Accidents/Criminal/SexCrime/Pedophilia/ChildPornography",
             "/?/Clothes/ClothingShoes/Clothing/Underwear"
        )),
        'drugs': Rule(cats=(
             "/?/Society/SocialEvils/DrugAddiction/DrugUseAndProduction",
             "/?/Society/SocialEvils/DrugAddiction/DrugUseAndProduction/LegalDrugsAndEntheogens",
             "/?/Society/SocialEvils/DrugAddiction/DrugUseAndProduction/Cannabis",
             "/?/Society/SocialEvils/DrugAddiction/DrugUseAndProduction/Cannabis/CannabisCultivation",
             "/?/Society/SocialEvils/DrugAddiction/DrugUseAndProduction/DrugProduction",
             "/?/Society/SocialEvils/DrugAddiction/DrugUseAndProduction/DrugProduction/DrugRecipes"
         )),
        'suicide': Rule(cats=(
             "/?/Accidents/Suicide",
        )),
        'alcohol': Rule(cats=(
             "/?/Food/Drinks/StrongDrinks",
             "/?/Health/Med/Psychiatry/Addictology/Alcoholism",
             "/?/Society/SocialEvils/Alcoholism" 
        )),
        'smoking': Rule(cats=(
             "/?/Society/SocialEvils/Smoking/SmokingPropaganda",
             "/Society/SocialEvils/Smoking/SmokersRights",
             "/Food/TobaccoProducts/Cigarette",
             "/Food/TobaccoProducts/Cigar",
             "/Food/TobaccoProducts/Tobacco",
             "/Food/TobaccoProducts/SmokingAccessories"   
        )),
        'violence': Rule(cats=(
             "/Violence",
             "/Accidents/Criminal/SexCrime",
             "/Accidents/Criminal/Murders" 
        )),
        'gamble': Rule(cats=(
             "/?/Leisure/Games/Gambling/Casino",
             "/?/Leisure/Games/Gambling/Casino/CasinoOnline",
             "/?/Leisure/Games/Gambling/Casino/SlotMachines",
             "/?/Leisure/Games/Gambling/Lottery",
             "/?/Leisure/Games/Gambling/Bookmakers",
             "/?/Leisure/Games/Gambling/GamblingCardGames",
             "/?/Leisure/Games/Gambling/GamblingCardGames/Poker",
             "/?/Leisure/Games/BoardGames/CardGames/GamblingCardGames",
             "/?/Leisure/Games/BoardGames/CardGames/GamblingCardGames/Poker"
        )),
        'dating': Rule(cats=(
             "/?/Leisure/PersonalLife/Dating",
        )),
        'abuse_strong': Rule(cats=(
             "/Abuse/Obscene",
        )),
        'abuse_medium': Rule(cats=(
             "/Abuse/RoughAbuse",
             "/Abuse/EnglishAbuse/Obscene"
        )),
        'abuse_light': Rule(cats=(
             "/Abuse/LightAbuse",
             "/Abuse/EnglishAbuse" 
        )),
        'extremism': Rule(cats=(
             "/Society/Extremism/ExtremistMaterials/Texts",
             "/_LIGHT/Society/Extremism/ExtremistMaterials/Texts"
             "/?/Society/Extremism/ExtremistMaterials/Abuse",
             "/?/Society/Extremism/ExtremistMaterials/Titles/Video_Titles",
             "/?/Society/Extremism/ExtremistMaterials/Titles/NotListedVideo_Titles",
             "/?/Society/Extremism/ExtremistMaterials/Titles/Music_Titles",
             "/?/Society/Extremism/ExtremistMaterials/Titles/Sites",
             "/?/Society/Extremism/ExtremistMaterials/PoliticalExtremism",
             "/?/Society/Extremism/Nationalism",
             "/?/Society/Extremism/ExtremistMaterials/Islamism",
             "/?/Society/Extremism/Nationalism/Antifascism",
             "/?/Society/Extremism/Nationalism/Neopaganism",
             "/?/Society/Extremism/Nationalism/Racism",
             "/?/Society/Extremism/Nationalism/Skinheads",
             "/?/Society/Extremism/Nationalism/FarRight",
             "/?/Society/Extremism/ReligiousIntolerance",
             "/?/Society/Extremism/ExtremistMaterials/Titles",
             "/_STRICT/Society/Extremism/ExtremistMaterials/Titles"                    
        )),
        'sects': Rule(cats=(
             "/Society/Religion/Sects",
              
        )),
        'explosives': Rule(cats=(
             "/Society/Security/Explosives",
             "/Society/Security/Explosives/Smokes",
             "/Society/Security/Explosives/ExplosivesProduction",
             "/Society/Security/Explosives/ExplosivesTrade",
             "/Society/Security/Weapon/Firearms",
             "/Society/Security/Weapon/Firearms/NonLethal",
             "/Society/Security/Weapon/PneumaticWeapons",
             "/Society/Security/Weapon/GasWeapons",
             "/Society/Security/Weapon/ProjectileWeapons",
             "/Society/Security/Weapon/ColdWeapons",
             "/Society/Security/Weapon/ElectroshockWeapons",
             "/Society/Security/Weapon/WeaponsProduction",
             "/Society/Security/Weapon/WeaponsTrade",
             "/Leisure/Holidays/Pyrotechnics/ManufactureOfPyrotechnics",
             "/Leisure/Holidays/Pyrotechnics/SaleOfPyrotechnics",
             "/Leisure/ActiveLife/Paintball/Airsoft",
             "/Leisure/ActiveLife/Paintball/Airsoft/AirsoftGear"
             "/Society/Security/Weapon",
             "/_LIGHT/Society/Security/Weapon",
             "/_LIGHT/Society/Security/Explosives"
        ))
      }

  def match(self, metacat, cats):
    if metacat in self.rules:
        return self.rules[metacat].match(cats);
    else:
        return []
