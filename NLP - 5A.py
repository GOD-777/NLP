
from inltk.inltk import setup
setup('hi')


import inltk
from inltk.inltk import tokenize
'''
from inltk.inltk import setup
setup('hi')
'''
hindi_text = """ाचीन काल मिवमा
दय नाम के एक आदश राजा आ करते थे। अपने साहस, पराम और शौय के िलए राजा िवम मश"र थे। ऐसा भी कहा जाता है 
क राजा िवम अपनी ाजा के जीवन के दखु दद जानने के िलए रा(ी के पहर म	भेष बदल कर नगर म	
घूमते थे।"""
# tokenize(input text, language code)
print(tokenize(hindi_text, "hi"))

