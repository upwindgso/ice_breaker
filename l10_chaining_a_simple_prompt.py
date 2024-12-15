
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

information = """
Raymond Thomas Dalio (born August 8, 1949)[1] is an American investor and hedge fund manager, who has served as co-chief investment officer of the world's largest hedge fund, Bridgewater Associates, since 1985. He founded Bridgewater in 1975 in New York.[2][3]

Dalio was born in New York City and attended C.W. Post College of Long Island University before receiving an MBA from Harvard Business School in 1973. Two years later Dalio launched Bridgewater.

In 2013, Bridgewater was listed as the largest hedge fund in the world.[4][5] In 2020 Bloomberg ranked him the world's 79th-wealthiest person.[6] Dalio is the author of the 2017 book Principles: Life & Work, about corporate management and investment philosophy. It was featured on The New York Times bestseller list.[7][8]

As per the March 2024 Forbes Global Wealth list, Ray Dalio ranked #123 with a net worth of $15.4 Billion.[9]

Early life
Dalio was born in the Jackson Heights neighborhood of New York City's Queens Borough.[10] When he was 8, the family moved from Jackson Heights to Manhasset in Nassau County, New York. He is the son of a jazz musician, Marino Dallolio (1911–2002), who "played the clarinet and saxophone at Manhattan jazz clubs such as the Copacabana," and Ann, a homemaker.[10][11][12] He is of Italian descent. He attended Herricks High School.[13]

According to Dalio, he caddied at The Links Golf Club, which was within walking distance of his childhood home. He caddied for many Wall Street professionals during his time there, including Wall Street veteran George Leib. Leib and his wife Isabelle invited Dalio to their Park Avenue apartment for family dinners and holiday gatherings.[14] The couple's son, a Wall Street trader, later gave Dalio a summer job at his trading firm. According to Dalio, he began investing at age 12, when he bought shares of Northeast Airlines for $300 and tripled his investment after the airline merged with another company.[15] He received a bachelor's degree in finance from Long Island University (C.W. Post College). After graduating from C.W. Post College, Dalio worked as a clerk on the New York Stock Exchange.[13]

He received a MBA from Harvard Business School in 1973.[15][16]

Investment career
According to Dalio, his early investments were in commodity futures. Commodity futures had low borrowing requirements at the time, and Dalio knew he could profit more handsomely than with simple stocks.[17]

During his time at Harvard, Dalio and his friends created the company that later became Bridgewater Associates. Its goal was to trade commodities. The venture yielded little fruit.[13] Dalio later used the name Bridgewater for his hedge fund.[18]

After graduating from Harvard, Dalio moved to Wilton, Connecticut, where he traded out of a converted barn.[10] He then worked on the floor of the New York Stock Exchange and traded commodity futures.[15] He later worked as the Director of Commodities at Dominick & Dominick LLC.[19] In 1974, he became a futures trader and broker at Shearson Hayden Stone, a securities firm[15] run by Sandy Weill, who later became famous for building up Citigroup. At the firm, Dalio's job was to advise cattle ranchers, grain producers, and other farmers on how to hedge risks, primarily with futures.[20] Dalio was fired from Shearson Hayden Stone after punching his boss in the face while drunk at a New Year's Eve party in 1974.[20]

Founding of Bridgewater Associates
In 1975, he founded Bridgewater Associates.[21] Bridgewater started out as a wealth advisory firm, in which capacity it served numerous corporate clients, mostly retained from Dalio's job at Shearson Hayden Stone.[13] The main areas in which Dalio advised were currencies and interest rates. The company began publishing a paid subscription research report, Daily Observations, in which it analyzed global market trends.[22] Dalio's big break came when McDonald's signed on as a client of his firm. Bridgewater then began to grow rapidly. The firm signed on larger clients, including the pension funds for the World Bank and Eastman Kodak.[7] In 1981, the firm opened an office in Westport, Connecticut, which was where Ray and his wife wanted to start a family.[13] Dalio started to become well-known outside of Wall Street after turning a profit from the 1987 stock market crash. The next year, he appeared on an Oprah Winfrey Show episode titled "Do Foreigners Own America?"[7] In 1991, he launched Bridgewater's flagship strategy, "Pure Alpha", a reference to the Greek letter that, in Wall Street terminology, represents the surcharge a money manager can earn above a particular market benchmark, such as the NASDAQ.[23] In 1996, Dalio launched All Weather, a fund that pioneered a steady, low-risk strategy that later became known as risk parity.[7]

Rise to prominence

Bridgewater Assoc. Pure Alpha I stock market strategy returns vs the S&P 500.
Bridgewater Associates became the world's largest hedge fund in 2005.[21] From 1991 to 2005, it lost money in only three calendar years, and never more than 4%. During the same period, the S&P 500 also had three down years, including a negative return of 22.1% in 2002.[24] The fund grew in size by using the standard hedge fund model, which takes a 2% management fee of assets and 20% of yearly profits accrued from using an investment system.[25] By 2005, Dalio was managing money for extremely large entities, including the $196 billion California Public Employees' Retirement System (CalPERS), the $27 billion Pennsylvania State Employees' Retirement System (Penn SERS or SERS), Melbourne-based National Australia Bank Ltd. and the pension fund of Hartford, Connecticut-based United Technologies Corp.[24] In 2007, Bridgewater predicted the 2007–2008 financial crisis,[10] and in 2008, Dalio published "How the Economic Machine Works: A Template for Understanding What is Happening Now", an essay assessing the potential of various economies by various criteria.[26] The firm's total assets under management increased to $50 billion in 2007 (up from $33 billion seven years earlier).[27]

According to a 2007 article in Barron's magazine, "nobody was better prepared for the global market crash" than Bridgewater's clients and subscribers to its Daily Observations. The company "began sounding alarms...in the spring of 2007 about the dangers of excessive financial leverage."[28] Researchers at the firm examined the public records of most of the world's largest financial entities and discovered that estimated future liabilities related to bad debts totalled $839 billion. When Dalio met with U.S. Treasury Department staff and other White House economic advisors in December, these findings were disclosed but were largely ignored.[10] Due to this research, Bridgewater's Pure Alpha fund avoided much of the 2008 stock market implosion for its investors.[29] In 2008, a disastrous year for many of Bridgewater's rivals, the firm's flagship Pure Alpha fund rose in value by 9.5% after accounting for fees.[10] Dalio did this by anticipating that the Federal Reserve would be forced to print a lot of money to revive the economy. He went long on Treasury bonds, shorted the dollar, and bought gold and other commodities.[10] During his 2008 presidential campaign, John McCain paid a visit to the firm and spoke to staff.[30] The next year was not as bright. In 2009, when economic growth was higher than expected and the Dow Jones Industrial Average increased by 19%, the company's Pure Alpha fund reportedly earned just 2% to 4%.[29]

In 2011, Dalio self-published a 123-page volume, Principles, that outlines his philosophy of investment and corporate management.[31][32] By that same year, Dalio was managing money for the SERS, Kodak, General Motors and the Government Investment Corporation of Singapore.[10] In 2012, he appeared on the annual Time 100 list of the 100 most influential people in the world.[33] In 2011 and 2012, Bloomberg Markets listed him as one of the 50 Most Influential people. Under Dalio's leadership, Bridgewater's Pure Alpha II had just three losing years in its history, with an average return of 10.4%. A stake in Bridgewater Associates Intermediate Holdings, LP was purchased by the Teacher Retirement System of Texas (TRS) for $250 million in February 2012. This stake was non-voting and thus provided the pension fund with very little control of corporate governance.[34] Institutional Investor's Alpha ranked Dalio No. 2 on its 2012 Rich List.[35][36] Dalio has controlled Bridgewater Associates alongside co-chief investment officers Bob Prince and Greg Jensen since its inception. The hedge fund recently announced plans to reorganize as a partnership. Dalio said the reason for this was the continued sustainability and profit-sharing of the company.[37] Dalio was co-CEO of Bridgewater for 10 months before announcing in March 2017 that he would step down as part of a company-wide shakeup by April 15.[38] The company had been in a seven-year management and equity transition to find a replacement.[39] Jon Rubinstein, co-CEO of the fund, was announced to step down with Dalio, but would retain an advisory role.[38] As of October 2017 Bridgewater Associates had $160 billion in assets under management.[40] In reference to the personality that led him to investment success, Dalio has said that he considers himself a "hyperrealist", and that he is motivated to understand the mechanisms that dictate how the world actually functions, without adding in abstract value judgments.[25]

Investment philosophy
According to Dalio, Bridgewater Associates is a "global macro firm",[41] investing around economic trends, such as changes in exchange rates, inflation, and G.D.P. growth.[10] Dalio has said he divides his holdings into two different areas: beta investments and alpha investments.[42] Beta investments produce returns through passive management and normal market risk. Alpha investments are actively managed and aim to generate better returns than beta investments. Alpha investments are not related to the general market.[27] Dalio's goal is to structure portfolios with uncorrelated investment returns based on risk allocations rather than asset allocations. Dalio's hedge fund mostly accepts money from institutional clients such as pension funds, foundations, endowments, and central banks.[10][43] Private investors can rarely invest in Dalio's holdings.[10][43][25]

According to Dalio, his strategy mainly focuses on currency and fixed income markets.[25] This is in contrast to buying individual shares in companies, like investors such as Warren Buffett and Peter Lynch.[25] Dalio also popularized the risk parity approach,[44] which he uses for risk management and diversification within Bridgewater Associates. Dalio employs an investment strategy that blends conventional diversification with "wagers on or against markets around the world" according to Bloomberg.[43] Dalio's risk parity approach allows for both leverage and external diversification when investing, as well as short selling. This allows Dalio to use any asset combination he chooses when investing.[45] Dalio's strategy uses an optimal risk target level as its basis for investing. This is in contrast to first allocating capital and then achieving a risk target. Dalio implements this strategy by using leverage to evenly distribute exposure across various asset classes while maintaining the best risk target level.[45] Dalio began using the term "d-process" in February 2009 to describe the deleveraging and deflationary process of the subprime mortgage industry as distinct from a recession, and subsequently incorporated the term into his investment philosophy.[28] Dalio's exact investment portfolios are largely kept a secret from the outside world. This includes most employees, as well as external investors, and only a dozen people within his firm understand how it trades at a given time.[7]

Controversy
A November 2023 New York Times investigative report, based on the book by the paper's finance journalist Rob Copeland,[46] raised questions about claims that Dalio and the fund had made about its investment philosophy and investment methodology.[47] For example, the report indicated that the fund's investments are based largely on Ray Dalio's own picks, not by the sophisticated investment system that Dalio and the firm had touted; and that investment choices are driven by insider information, legally obtained, derived from Dalio's personal associations with prominent government actors.[47] Dalio's lawyers threatened a multibillion-dollar lawsuit against the publisher MacMillan over what they allege is an inaccurate portrayal of the firm and Dalio.[48]

Views
Capitalism and socio-economic inequality
While Dalio has stated that capitalism is generally the best economic system, he has argued that it needs to be reformed due to it "not working well for most Americans".[49] On April 7, 2019, Dalio said on 60 Minutes that income inequality in the United States was a national emergency requiring reform.[50][51] In July 2019, he again called for the refinement of capitalism and called wealth inequality a national emergency.[52] In November 2019, he posted a blog entry stating that excess capital, unfunded social liabilities, and government deficits had created a recipe for disaster, in what he called a "paradigm shift".[53] In May 2020, he stressed the importance of reforming capitalism, not abandoning it, saying, "As the current crisis unfolds, we should remember that throughout history, capitalism has proven to be the best system, though it can sometimes be highly flawed."[54] In October 2020, Dalio said that there has been little income growth for average citizens over the preceding two decades, with the bottom 60% of workers having no inflation-adjusted income growth since the 1980s.[49] He mentioned that income inequality was at its highest level since the 1930s, when the top 1% of earners had more wealth than the bottom 99% combined.[55] Dalio said that the odds of a low-wage earner moving to a higher level of wealth were decreasing over time and that this demonstrated Americans' lower economic and social mobility. He warned that inequality was becoming more entrenched and rising fast.[49] He said that hypothetical improved capitalism would have to be good at creating a bigger pie and redistributing it as well.[54]

China
In October 2020, Dalio cautioned people to not be blind to China's rise,[56] arguing that it had continued to emerge as a global superpower. He claimed that China had succeeded in "exceptional ways", including high economic performance in spite of the COVID-19 pandemic, some of the lowest COVID-19 case rates, and being the center of half of all listed initial public offerings globally.[57][58] Dalio asserted that when he visited China in 1984, high-ranking officials would marvel at basic technology such as calculators, calling them "miracle devices". He argued that China was now on par with the U.S. in advanced technologies and would probably take the lead in the next five years.[57] In addition, Dalio said that there were many indicators that favored China.[57] He discussed the growing population of well-educated citizens, as well as China's continued growth in the absorption and processing of data, which many headlines have called "the new oil".[59][60] Dalio also called China favorable from an investor's perspective. He said that the Chinese economy's fundamentals were strong and its assets relatively attractively priced.[56][57] Dalio also maintained that China's stocks and bonds were currently underweighted in terms of the global portfolio, and that the U.S. was bloated.[57] A natural shift in pricing would give China another comparative advantage. While stressing that things could always go wrong, Dalio stated that he believed China's path of economic reform would continue, bringing it unabated prosperity.[56][57] He also downplayed and denied Chinese human rights violations, instead likening the Chinese government to a "strict parent". Dalio's stance on China has garnered criticism.[61][62]

Principles
To follow the 2017 New York Times bestseller Principles: Life & Work, Dalio published an illustrated version in 2019 called Principles for Success.[63] Dalio also published Principles for Navigating Big Debt Crises in 2018 and Principles for Dealing with the Changing World Order in 2021.[64][65] In 2021 Dalio produced a free online personality assessment called PrinciplesYou.[63]

Personal life

Ray Dalio at the International Achievement Summit's 2012 Banquet of the Golden Plate reception in Washington, D.C., with his wife, Barbara, and two Academy of Achievement student delegates, Philip Thigo of Kenya and Julia Fan Li of Canada
Family
Dalio lives with his wife Barbara, a descendant of sculptor Gertrude Vanderbilt Whitney,[10] in Greenwich, Connecticut.[15] They have four sons.[11] Their oldest son, Devon, died in an automobile accident in 2020 at age 42.[66] Their second son, Paul Dalio (born 1979), is a film director.[67]

Health
Dalio has suffered from Barrett's esophagus, a form of gastroesophageal reflux disease (GERD), a pre-malignant condition that if not treated properly can lead to cancer.[68]

Wealth
In 2014 he reportedly earned $1.1 billion, including a share of his firm's management and performance fees, cash compensation and stock and option awards.[69] In 2015, Forbes estimated his net worth at $15.4 billion, making him the second-wealthiest hedge fund manager after George Soros.[70] In 2018, Dalio was estimated to have personally received $2 billion in compensation for the year, after his fund posted a 14.6% return.[71] In March 2019, Forbes named Dalio one of the highest-earning hedge fund managers and traders.[72]

According to Forbes, Dalio has an estimated net worth of $20 billion as of January 21, 2022, ranking him 88th on their billionaires list[73] and 36th on the Forbes 400 list.[74] In January 2022, Bloomberg News reported Dalio's net worth as $15.7 billion, making him the world's 123rd-richest person according to their rankings.[75]

Philanthropy
Duration: 3 minutes and 36 seconds.3:36
Dalio giving a speech on philanthropy
Overall, the Dalio family has donated more than $5 billion to his Dalio Foundation,[76] and the foundation has given out more than $1 billion in charitable grants.[77] In April 2011, Dalio and his wife joined the Giving Pledge, vowing to donate more than half his fortune to charitable causes within his lifetime.[78]

Dalio has sat on NewYork–Presbyterian Hospital's board of trustees since 2020.[79] In February 2020, the Dalio Foundation donated $10 million to support China's coronavirus recovery efforts in response to the COVID-19 pandemic. In March 2020, the foundation gave $4 million to the state of Connecticut to fund healthcare and nutrition.[80] On October 13, 2020, NYP launched the Dalio Center for Health Justice[81][82] with a gift of $50 million.[83]

The foundation has supported the Fund for Teachers,[84] David Lynch Foundation,[85] National Philanthropic Trust,[86] and TED's Audacious Project.[87] Dalio's research yacht and submarine have appeared on the Discovery Channel during Shark Week and have been used to hunt for a giant squid.[70] In 2018, OceanX, an initiative of the Dalio family, and Bloomberg Philanthropies[88] committed $185 million over four years to protect the oceans.[89] In 2019, he pledged $100 million to Connecticut public schools.[90]

Dalio has backed the Volcker Alliance, the public policy group headed by former Federal Reserve chair Paul Volcker.[70]

Hobbies
He practices Transcendental Meditation.[17] He is an avid outdoorsman, and enjoys both hunting and fishing. He has hunted cape buffalo, grouse, elk, and warthog.[80] He is especially fond of bow-hunting, the bow being his weapon of choice when hunting
"""

if __name__ == "__main__":
    print("Hello world")

    summary_template = """
        given the {information} about a person I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"]
        ,template=summary_template
        )

    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})

    print(res)
    
    




