# *Honest Quantitative Trading: A First Lesson for Beginners*

---

# Preface: A Few Words Before We Begin

## This Book Is for You, Just Starting Out

If you opened this book, it is probably because you have heard the phrase “quantitative trading” and found it both mysterious and tempting: people write some code, run some data, and somehow get computers to make money for them. You may know nothing about statistics, have never written a line of code, or have never even heard of an “order book.” That is fine. This book was written for you at exactly this point.

I assume only a little everyday common sense: stocks rise and fall, buying and selling incur fees, and there is no such thing as a free lunch. Beyond that, I assume no background knowledge. The first time any technical term appears, I will explain it in plain language and with an everyday analogy before using it. You do not need to study elsewhere first; just read along.

## Why This Book Is Needed Among All the “Get Rich Quick” Lessons

Search for “quantitative trading,” and you will probably be flooded by courses promising “$100,000 a month,” “consistent profits,” and “financial freedom.” They all have one thing in common: first they sell you a dream, then they sell you a method.

This book does not sell that dream. Here is the conclusion up front: this is hard. Markets are nearly efficient, and any obvious money-making pattern is quickly picked up by people who are smarter, wealthier, or faster—like a hundred-dollar bill on the ground in a busy downtown, gone in less than a second. After fees and all the invisible costs are deducted, most active traders struggle to outperform an appropriate benchmark over the long run.

So why is it still worth learning? Because markets are only *nearly* efficient, not perfectly efficient. Constraints, risk, capacity, and execution frictions can still leave clues worth researching—but a clue is not automatically your profit. This book will not teach you how to get rich overnight. It will teach you how to judge honestly whether a clue has evidence behind it, whether it can cover its costs, and how to stay alive when that judgment turns out to be wrong.

## Three Principles for the Whole Book

This book grows out of the daily work of a quantitative research lab. It is organized around three principles:

**Survive first, then think about winning.** A single devastating loss can wipe out years of progress. So this book begins with how to limit losses and preserve continuity before discussing how to find an edge.

**A negative result is knowledge, not failure.** Most ideas will not pass testing. As long as the question is clear, the test is honest, and the conclusion is recorded, ruling out a wrong direction is progress.

**The tools of a pessimist, the heart of an optimist.** In method, estimate fills, costs, and risk under adverse conditions; in spirit, do not stop asking the next, better question just because one idea has been rejected. Later chapters will turn each of these three sentences into rules you can follow.

## What This Book Is Not

To respect your time, I should also be clear about what this book will not give you:

- **It is not a guide to getting rich quickly.** There is no shortcut here to “tenfold returns in three months.” If that is what you want, you have opened the wrong book—and will probably pay tuition far more expensive than its price.
- **It does not give you ready-made trade calls.** I will not tell you “which stock to buy, when to enter, or when to exit.” This book teaches methods and discipline that can be used repeatedly over the long term, not one-off answers.
- **It does not guarantee profits.** No book or strategy can guarantee that you will make money. This book can only help you avoid some of the mistakes that would end your research prematurely.
- **It is not a programming book or a mathematics textbook either.** We will use some statistical intuition, but I promise to explain it plainly before introducing formulas, and never bury you under a pile of symbols.

# How to Read This Book

## A Map of the Book: Five Parts

This book has sixteen chapters divided into five parts:

**Part I | What Game Is This? (Chapters 1–3).** First, see clearly what you are about to play: quantitative trading is not a crystal ball, but a discipline of placing bets; why markets are hard to profit from; and how research arrives at credible conclusions.

**Part II | The Foundations of Markets and Data (Chapters 4–5).** Explains how order books and liquidity affect execution, and how bad data distorts a backtest.

**Part III | Turning Ideas into Testable Rules (Chapters 6–9).** The core craft of research: trim the vague intuition of “I think” into a hypothesis that can be disproved; test it with the time machine of backtesting; use statistical rigor to distinguish real skill from pure luck; and finally turn it into a rule a machine can follow every day.

**Part IV | Learn to Survive First (Chapters 10–13).** The center of gravity of the book: how much real execution costs; how risk management keeps you alive; what genuine diversification in a portfolio looks like; and how to cross the irreversible threshold from paper research to live trading with real money.

**Part V | Mindset and the Long Road (Chapters 14–16).** Discusses human biases outside the code, how to preserve negative results, and how to choose problems that fit your own circumstances.

## A Suggested Reading Order

I wrote this book as a gradual journey, so **my strongest recommendation is to read straight through from Chapter 1 to Chapter 16.** Each chapter uses ideas laid down earlier, and skipping around makes it easy to lose your footing.

If you can read only a few chapters first, start with **Chapters 1, 2, and 11**. The first two explain quantitative trading and market competition; Chapter 11 focuses on risk management.

As for the more method-focused chapters in Part III, if they feel demanding on a first read, give yourself permission to grasp the main idea first and return to the details later. This is a book to revisit, not one to read once and put on a shelf forever.

## What Each Chapter Looks Like

To make reading easier, every chapter follows the same structure. Make use of it:

- **Opening**: Introduces the problem through a scene or a common misconception.
- **Main text**: Explains the chapter’s concepts and illustrates them with examples.
- **⚠️ Common Pitfalls**: Lists judgments and boundaries that are easy to confuse.
- **🔬 A Lesson from Practice** (in some chapters): Turns mistakes the lab encountered into cases that show how an error later became a rule.[^case-provenance]
- **📌 Chapter Takeaways**: A few sentences that gather the essentials. Come straight here when you want to review what you have read.
- **✍️ Try It / Think About It**: One or two small exercises or questions for reflection, meant to test whether you truly understood the chapter after reading it.

[^case-provenance]: These cases are organized from the author’s narrative materials. The underlying logs, code, and execution records have not been independently verified; they illustrate methods and should not be treated as reproducible empirical evidence.

## Three Mental Preparations for Beginners

Finally, before you set out, there are three things I want to tell you first, so that you do not trip yourself up halfway through:

**First, prepare before you trade.** This book will not have you trading tomorrow, nor does it encourage you to do so. Before you begin, write down your research method and risk discipline.

**Second, most ideas will not hold up.** That is normal. If the test is honest and its boundaries are recorded clearly, ruling out a wrong direction is still research progress.

**Third, make both curiosity and discipline into habits.** Curiosity generates questions; discipline rejects answers that lack sufficient evidence. Both must be built into a repeatable process.

## Safety and Disclaimer

Finally, a few points that must be made clear:

This book is solely for **educational and knowledge-sharing purposes**, intended to help complete beginners build sound concepts and research methods. Nothing in it—including any strategies, examples, or figures—**constitutes investment, financial, or trading advice**, nor is it a recommendation to buy or sell any financial product.

Trading involves real financial risk. **Any strategy can lose money, and you may lose some or even all of your principal.** Past performance (including any backtest result) does not guarantee future profit. The examples in this book are simplified to illustrate concepts and must not be copied directly into live trading.

Before putting any real money to work, fully understand the risks you are taking, use only spare money you can afford to lose, and consult qualified professionals when needed. This book can help you lay a solid foundation of ideas and discipline, but every final decision—and its consequences—remains your own responsibility.

All right: the caveats are now out in the open. Turn the page, and we will begin with “What exactly is quantitative trading?”

---

# Chapter 1: Quantitative Trading—Seeking a Long-Term Edge in an Uncertain World

## What You Think Quant Is, and What It Actually Looks Like

Popular accounts of quantitative trading tend to reuse the same images: a genius before six monitors, a mysterious program calculating which stock will rise tomorrow, and a machine moving money into its owner's pocket without ever making a mistake.

That picture treats quantitative trading as a form of prediction. To see its real logic, first distinguish a casino from a gambler: quant is closer to operating the casino than to placing a bet in the moment.

A gambler cares whether they will win this hand; a casino cares whether, over the next ten thousand hands, it will win on average. A casino does not need to win every hand. It relies on rules written in advance, a small edge, many repetitions, and limits on losses to sustain its long-run results.

Quantitative traders adopt exactly this perspective: rather than predict the next hand, they write the probabilities, position sizes, and losses across many bets into rules. Let us begin by asking what those “rules” actually are.

## What Is Quantitative Trading? Replacing “Market Feel” with “Rules + Data”

First, let us make the terminology clear.

**Quantitative trading** and **systematic trading** overlap heavily, but they are not exact synonyms. The former emphasizes data, models, and computation; the latter emphasizes making decisions according to a prewritten system. To keep things accessible for beginners, this book uses “quantitative trading” as a broad term: using clear rules and data to decide when to buy and sell, rather than relying on in-the-moment “feelings.”

Start with an everyday analogy. A fruit seller who has worked at the entrance to an alley for thirty years can heft a watermelon and tell whether it is sweet. That experienced intuition may be accurate; the problem is that it is difficult to explain, verify, or teach to someone else, and it may fail when the seller's condition changes.

Quantitative trading turns that judgment into recorded rules—for example, specifying thresholds for weight, sound, and rind pattern. Once written down, the rules can be checked; given the same data, code, and execution conditions, other people should obtain a verifiable result.

In markets, these “rules” do not determine whether a watermelon is sweet; they determine whether “now is the time to buy, sell, or stay put.” The “data” fed into the rules are the traces left by the market: price, volume, time, and so on.

The core of quant is simple: **translate vague intuition into clear rules, then test those rules with data.**

## How Is It Different from Discretionary Trading? Backtestable, Reproducible, and Less Emotional in the Moment

So how exactly is it different from buying and selling by feel, which we call **discretionary trading**? The difference lies in three very practical areas.

**First, it is backtestable.** Once the rules are written clearly, you can run them through historical data to simulate what would have happened in the past. A discretionary trader’s “feeling at the time” is hard to replay exactly; quantitative rules can be tested repeatedly. Chapter 7 will fully explain why backtests are both useful and dangerous.

**Second, it is reproducible.** Given the same data, parameters, code version, and execution assumptions, you today, you tomorrow, and a stranger on the other side of the world should be able to reproduce the same result. That means success and failure can be traced, and the system can be improved step by step.

**Third, it can reduce emotions rewriting decisions in the moment.** When a stock is falling, it is easy to change a previously agreed stop-loss into “let’s wait a little longer.” After making a profit, it is also easy to get carried away and increase the position until it is out of control. Quant cannot eliminate emotion, but it can put as much of “what to do” as possible into rules in advance, leaving less room for fear and greed to seize control at the last minute.

Many beginners think the value of quant is “calculating more accurately than everyone else.” More often, and more practically, its value is making judgments inspectable, setting risk boundaries in advance, and reducing the chance that an impulse changes your rules for you.

## Busting Three Misconceptions First

Rule-based decisions can be backtested and reproduced, and they reduce the temptation to rewrite a decision in the moment. But these benefits are also often exaggerated. Before turning to a concrete example, let us clear up three misconceptions: quant is not the same as high-frequency trading, AI prediction, or guaranteed profits.

**Misconception 1: Quantitative trading is high-frequency trading—the kind that places thousands of trades per second.**
It is not. High-frequency trading is indeed one branch of quant, and it often requires expensive infrastructure, extremely low latency, and detailed market microstructure models. But quant also includes low-frequency strategies that adjust positions only once a day, every few days, or even every few weeks. Speed is a feature of a strategy, not the definition of quant. You do not need a supercomputer; an ordinary laptop is enough to begin research—just do not use it to enter an arms race over latency.

**Misconception 2: Quant means using the most advanced AI to make uncannily accurate predictions.**
Artificial intelligence is only one of the tools quant can use. Research quality depends more on whether the data fit the problem, the objective is clearly stated, and the testing is honest. Many failures do not occur because the model is “not smart enough,” but because the data are wrong, labels peek into the future, costs are omitted, or the researcher tries too many things on the same history. New tools cannot repair methodological errors.

**Misconception 3: Quant is a money-printing machine with guaranteed profits.**
**There is no strategy with guaranteed profits.** Any product or method that claims otherwise should be treated as a major warning: it may be concealing risk, or it may not understand its own model correctly. Quant does not eliminate risk; it can only help people identify, estimate, and manage it. Tail losses and their probabilities often cannot be known precisely, so risk management must also account for estimation error.

Until these three misconceptions are cleared away, everything that follows will rest on the wrong expectations.

> **⚠️ Common Misconceptions**
>
>
> **Misconception 1: “I want to find a strategy with a 90% win rate.”**
> A high win rate does not mean a strategy makes money. If a strategy earns $1 on nine out of ten trades but loses $20 on the tenth, its win rate is 90%, yet the total result is a loss of $11. Evaluating a strategy also requires examining the size of gains and losses, tail losses, and its ability to withstand consecutive losses.
>
>
> **Misconception 2: “These rules made money for the last ten years, so they must work.”**
> Attractive historical results may simply mean the rules were repeatedly adjusted until they fit past noise. This is called **overfitting**; Chapter 8 will unpack it fully. For now, remember: past profits are not proof that a strategy will work in the future.

## A Concrete Example: What Rules Look Like

With those misconceptions cleared away, a simple **moving-average crossover** can show how a vague judgment is turned into a rule.

First, what is a moving average? A “20-day moving average” adds up the closing prices from the most recent 20 days and divides by 20, producing an average price. It is calculated each day and connected into a line. Think of it as the stock price’s “recent temperature”: it smooths out day-to-day noise so that you can see the general direction. Similarly, a “60-day moving average” is the average over the most recent 60 days, reflecting a longer-term, slower trend.

All right, here are the rules—just two sentences:

- **When the 20-day moving average crosses above the 60-day moving average—buy.**
- **When the 20-day moving average crosses below the 60-day moving average—sell.**

The intuition is this: when the short-term moving average crosses above the long-term one, recent momentum has begun to exceed longer-term inertia, perhaps marking the start of an uptrend. When it crosses below, the trend may be weakening.

At this point, a vague judgment about trend has become two entry-and-exit rules that a computer can execute and a researcher can backtest. Strictly speaking, they still lack execution timing, position size, costs, and handling for unusual conditions; later chapters will add those pieces. Given the same price data and calculation conventions, anyone should identify the same crossover points.

Do not treat these two sentences as a ready-to-trade answer. A moving-average crossover can produce completely different results across markets, periods, parameters, and cost assumptions. Sometimes it captures trends; sometimes it repeatedly generates false signals in a range-bound market. It appears here only to show how a vague judgment becomes a testable rule. Chapter 6 will go further and show how to state a rule as a hypothesis that data can disprove.

## So What Do Quantitative Traders Actually Earn?

If they are not making money by guessing correctly, then what are they relying on?

The answer lies in the casino analogy at the beginning. Quantitative traders do not earn money from “guessing this hand right.” They earn money from **“holding even a tiny probabilistic edge over the long run and across many bets, while managing risk with discipline.”**

Now reduce the edge to a number. Suppose buying under certain conditions produces an average return of 0.5% per trade. That is an average across many trades; any individual trade can still make money or lose it.

If that average 0.5% edge still exists after costs, the sample is not crowded entirely into one type of market environment, and the mechanism producing the edge does not quickly disappear, then repeated execution may gradually reveal that edge in the average result. The law of large numbers will not create profits from a bad model, nor does it guarantee that tomorrow will follow yesterday’s distribution. It only reminds you that a small edge must be evaluated over enough relatively comparable trials; you cannot draw conclusions from one or two wins or losses. You do not need to win every hand, but you must be able to withstand the losses when bad luck comes in a row.

For an average edge to become a tradable long-run result, at least two conditions must hold:

First, the edge must survive testing. Chapters 7 through 10 will examine backtesting, statistics, rule implementation, and transaction costs, helping distinguish repeatable evidence from sampling luck. If the edge is not real, repetition merely repeats the same mistake many times.

Second, risk must allow the account to survive long enough. Even when an edge is real, it cannot pay off if one oversized position or one refusal to admit error knocks the account out first. Beginning with Chapter 11, “survive first, then think about winning” will be translated into position sizing, circuit breakers, and deployment boundaries.

## You Are a Scientist, Not a Gambler

By now, the outline of quantitative trading should be clear: it is not a crystal ball for predicting the future, but a set of rules repeatedly executed under uncertainty. It does not ask, “Can I guess this trade right?” It asks, “Can the rules be tested? Can the results be verified? Can losses be contained?”

This also explains why quantitative trading resembles scientific work more than gambling. A gambler treats one win or loss as an answer; a researcher treats one result as evidence. If a rule performs well, they ask whether the data, costs, or luck caused it. If it performs poorly, they do not immediately invent excuses to save it.

Chapter 3 will develop this approach into a complete research cycle. For now, retain this dividing line: **gamblers rely on feelings in the moment; quantitative researchers rely on rules written clearly in advance and auditable afterward.**

> **📌 Chapter Takeaways**
>
>
> 1. Quantitative trading uses “clear rules + data” to make buy-and-sell decisions rather than relying on market feel; it manages probabilities rather than predicting the future.
> 2. Compared with discretionary trading, quant has three major advantages: it is backtestable (it can be tested with historical data), reproducible (the same inputs and versions should reproduce the same results), and less prone to decisions being rewritten by emotion in the moment.
> 3. Bust three misconceptions: quant is not the same as high-frequency trading, AI-powered perfect prediction, or guaranteed profits. There is no holy grail—only understanding and managing risk.
> 4. A moving-average crossover is the simplest demonstration of “rule-based” trading. The point is not to claim that it makes money, but to understand what it means to translate intuition into testable rules.
> 5. Quantitative traders do not profit by “guessing right,” but by “holding a small real probabilistic edge across many bets over the long term + managing risk strictly, and surviving until the edge pays off.”
> 6. Quantitative trading is more like scientific work: rules should be written in advance, results should be verifiable, and errors should be identifiable. You are managing long-term probabilities, not making single-trade prophecies.
>
>
> **✍️ Try It / Think About It**
>
>
> 1. **Write your market feel as rules.** Think back to a time when you “felt it would rise” or “felt it was time to get out,” and translate that thought into sentences a computer can execute: under what conditions do you buy? Under what conditions do you sell? If the conditions cannot be defined precisely, the idea is not yet ready to be tested.
> 2. **Think about the win-rate trap.** Suppose a strategy has a 95% win rate. It sounds tempting. Can you make up an example in which this “95% win-rate” strategy actually loses money over the long run? (Hint: think about how much it loses in that 5% of cases.) Once you understand this, you will have grasped the first glimmer of risk management.

---

# Chapter 2: Markets Are Nearly Efficient—Why Making Money Is So Hard

## The Hundred-Dollar Bill on the Ground

There is an old economist joke. Two professors are walking down the street when the younger one suddenly looks down and shouts, “There is a hundred-dollar bill on the ground!” The older professor does not even look and says calmly, “Impossible. If it were really a hundred-dollar bill, someone would have picked it up already.”

This joke is often used to tease economists for being rigid, but it points to the problem left by the previous chapter: even if a rule once worked, why does it gradually lose its edge once it becomes public, easy to understand, and easy to copy?

The reason is competition. If a reliable way to profit is obvious enough for everyone to discover, participants will quickly take the same action and thin out the original opportunity.

## How Competition Thins Out Public Edges

To see how an opportunity becomes thinner, begin with what happens to prices after competitors enter.

When a profitable pattern becomes obvious enough for everyone to see, a large crowd will rush in to do the same thing. They race to buy, pushing prices up; they race to sell, pushing prices down. The more people do it, the thinner the original price gap or predictability usually becomes, until it may be too thin even to cover costs. That is how competition picks up the “hundred-dollar bill.”

These faster-reacting, lower-cost, or better-resourced participants are often collectively called **smart money**: professional funds, market makers, high-frequency trading firms, and the like. The label does not mean they are always right. It only means they are better able to discover, execute, and scale a public opportunity. The market’s street sweepers make mistakes too, but obvious money usually will not wait for you alone to notice it.

The academic framework behind this idea is the **Efficient Market Hypothesis (EMH)**. For now, hold on to the shared intuition: public information is quickly processed by many participants and reflected in prices, so it is very hard to earn persistent risk-adjusted excess returns using only material that everyone can see.

Let me also introduce a keyword that will run throughout this book: alpha, or excess return. It means the return that remains relative to an appropriate benchmark after accounting for the relevant risks. If you buy the broad market and rise along with it, that does not automatically count as alpha. The Efficient Market Hypothesis reminds us that reproducible alpha is scarce and, once public, is easily thinned out by competition.[^alpha-boundary]

[^alpha-boundary]: Alpha should be measured against an appropriate benchmark, after controlling for relevant risk exposures and costs. Observed positive alpha may also result from estimation error, selection bias, or omitted risks; it does not automatically demonstrate skill.

## Why Markets Are Only “Nearly” Efficient

If public information is rapidly reflected in prices, why is there anything left to research? Because markets are only **nearly** efficient, not **perfectly** efficient. Different participants face different capital, institutional, risk, and execution constraints. Those differences leave narrow, conditional spaces for research.

A hundred-dollar bill in the middle of a busy street is unlikely to remain there long. A small coin that rolls into a drain crack, however, may be left alone because it is hard to retrieve, cannot accommodate much capital, or requires taking a particular risk. There may be no money in the mud. The analogy makes only one point: when opportunities exist, they often come with capacity, data, or execution conditions. Chapter 16 will discuss how to judge whether one suits you.

## After Costs, Active Trading Is More Like a Negative-Sum Game

Even a narrow opening must still pass the cost test. We need to be precise here: holding companies, bonds, or other assets does not make aggregate returns a zero-sum game. But among active traders competing to “beat everyone else” in the same market, relative returns before costs are roughly offsetting. Fees, taxes, bid-ask spreads, and slippage then continually take a cut, pushing the combined relative results below zero.

For now, simply recognize the names of these costs. Chapter 4 will explain how spreads, depth, and market impact emerge from the order book; Chapter 10 will put them into a full cost ledger for a trade. For now, remember one thing: **an edge must first cover transaction costs before it deserves to be called a tradable edge.**

The more often you trade, the more often costs are charged. So an idea that appears profitable can still lose more and more money if its margin is too thin and its turnover is too high.

## How Do Those “Triple Your Money in Three Months” Masters Appear?

Competition and costs explain why making money is difficult, but the way results are publicized often makes it look easier than it is. You have surely seen this online: someone posts a brokerage statement showing that they tripled their capital in three months, then starts teaching courses, selling signals, and recruiting students.

Here you need to pull the camera back and see **survivorship bias**: you see only those who survived and succeeded, not the denominator of people who failed, blew up, or deleted their accounts and left. As a result, you overestimate the probability of success.

Suppose ten thousand people each flip a coin ten times. Even if everyone is relying on luck alone, about ten of them will, on average, get heads ten times in a row. If only one of those records is shown, an extreme random result can easily be mistaken for skill.

Some market “masters” may simply be the lucky survivors among those ten thousand people. This does not mean there are no truly skilled traders in the world. It means that from one attractive brokerage statement alone, you **cannot** tell whether someone is genuinely skilled or simply happens to be at the lucky tail of the distribution. You cannot see the full denominator, and platforms and sharing mechanisms are more likely to put the winning trades and winning months in front of you.

This also explains why frequent active trading is especially unfriendly to individual investors. Costs take one layer first; chasing rallies, selling in panic, and doubling down in anger take another; survivorship bias then causes people to underestimate the first two. Even without assuming that every individual investor must lose money, this structure is enough to show that persistently beating an appropriate benchmark after costs is difficult, and one attractive brokerage statement is nowhere near enough to represent the whole distribution.

> **⚠️ Common Misconceptions**
>
>
> **Misconception 1: “This pattern is so obvious—get in quickly!”**
> The more obvious a pattern is and the more people can see it, the more carefully you should ask why competition has not already thinned it out, how much remains after costs, and whether the current result is merely noise. Public does not mean ineffective, but a public rule still requires a rigorous explanation of its mechanism and rigorous evidence.
>
>
> **Misconception 2: “He tripled his money in three months, so following him cannot go wrong.”**
> You are seeing a survivor, not the whole picture. Behind that one winner may be hundreds or thousands of people who lost everything and left—people you will never encounter. A brokerage statement does not prove skill; it proves only that “this person happened to survive this period.”

## This Is Not an Attempt to Discourage You

Explaining that “making money is hard” is not meant to talk you out of the field. It is meant to calibrate expectations. If you believe alpha is everywhere, you are more likely to take oversized positions, trade too often, or overestimate yourself after the first winning streak—only to be punished later by costs and the reversal of luck.

A more reliable expectation is this: tradable edges are often thin. After finding one, it must still pass many tests involving data, statistics, costs, and live execution. Even for full-time teams, research often consists largely of ideas that fail to pass. Rejecting an idea is not unusual; what is unusual is an idea that still leaves behind something clear enough, stable enough, and sufficient to cover costs after a series of attempts to disprove it. The online promise of “three simple steps and guaranteed monthly profits” leaves out every difficult gate.

Difficulty itself is not protection, and obscurity does not mean there is money to be made. It only means that competition, fixed costs, and capacity may differ among opportunities. Chapter 16 will discuss how to judge whether an opportunity fits your resources. For now, keep the simpler conclusion: **public, obvious money is hard to leave lying around, and every corner must still pass the tests of evidence and cost.**

The market is nearly efficient, but not equally efficient in every place and at every moment. That “nearly” is not a promise of riches; it is only a narrow gap that makes research possible.

> **📌 Chapter Takeaways**
>
>
> 1. Markets are “nearly efficient”: obvious, public, easily copied patterns are quickly thinned by competition and price adjustment, just as a hundred-dollar bill on the ground in a busy area is unlikely to remain there long.
> 2. The key word is “nearly”: markets are not completely efficient everywhere and at all times. Opportunities may still exist, but they may be small, hard to trade, and constrained by capacity.
> 3. For active traders, relative edges before costs are roughly offsetting; fees, spreads, and slippage then push aggregate results down further. The more frequently you trade, the more you must first prove that you can cover your costs.
> 4. Most retail investors lose money over the long term: the negative-sum cost structure, unchecked human behavior, and overconfidence compound one another.
> 5. Beware survivorship bias: you see only the “masters” who survived, not the denominator of those who blew up and left. A brokerage statement cannot prove skill.
> 6. “Hard” is part of the game’s setup, not a reason to quit or a moat. Obscurity is only a clue to be tested; in the end, you still need to examine the mechanism, evidence, costs, and capacity.
>
>
> **✍️ Try It / Think About It**
>
>
> 1. Question that “guaranteed-profit method.” Find a method you have heard about that claims guaranteed profits—perhaps a tip from a friend or an online course—and seriously ask yourself: if it really guarantees profits, why would its creator tell you about it, or even sell it to you, rather than quietly make a fortune alone? Write down your answer.
> 2. **Record your “it will definitely rise.”** Over the next week, whenever you think, “This will definitely rise” or “This will definitely fall,” immediately note it in your phone along with the current price. After a week, look back and count: how many of those thoughts were actually correct? This small practice of “write it down first, then verify it later” is the beginning of the skill Chapter 6 will formally teach.

---

# Chapter 3: What Quantitative Traders Actually Do: The Research Cycle and Credible Conclusions

## 🔬 115 Commits, 0 Experiments

For a while, the lab looked incredibly busy. Code changed every day, and features were completed one after another. Looking through the records, the team had made **115 code commits**. Judging by the volume of activity, nobody could say we were not working hard.

Then someone asked a simple question: “During this time, how many hypotheses about the market did we actually test?”

The answer was: **zero.**

All 115 commits had gone into tools, pipelines, and interfaces; none had tested a market hypothesis. After that day, the team began measuring progress with a different yardstick:

> **A high volume of activity cannot substitute for a credible conclusion.**

Real quantitative researchers do not spend most of their time in front of six screens, racing to press buttons. More often, they read data-quality reports, investigate why a test failed, turn an idea into a specification others can verify, and accept the conclusion that “this did not pass.”

If the unit of progress is a credible conclusion, then a quantitative trader's core job is research before it is order placement. This chapter lays out the cycle from question to conclusion and the evidence that each stage must leave behind.

## The Research Cycle

Placing orders is only the final, usually automated step in the research process. Before it, an idea must pass through six connected stages:

**Stage 1: Form a hypothesis.** For example: “Whenever Bitcoin suddenly drops late at night, it often rebounds in the next hour.” Here, a **hypothesis** is a proposition that has not yet been validated but can be tested. The first step is to turn vague intuition into a precise sentence.

**Stage 2: Find data.** Testing requires historical price and trade records. Exchange data may contain gaps, incorrect timestamps, or other quality problems; Chapter 5 examines them in detail.

**Stage 3: Backtest.** Put the clearly written rules into a simulation using historical data and see whether they can even survive the past. A backtest is a screening tool, not a guarantee of the future; Chapter 7 will focus on its limits.

**Stage 4: Try to disprove it.** After a backtest produces a beautiful curve, keep checking what kinds of error could have created it and what evidence would force you to abandon it.

**Stage 5: The risk-management gate.** Even if a strategy passes the earlier tests, a wall still stands between it and real money. This stage no longer asks, “How much does it make on average?” It asks about position size, drawdown, tail scenarios, and stop conditions: even if the estimate is wrong, can the system still keep losses within an acceptable range? Chapter 11 focuses on risk boundaries.

**Stage 6: Iterate.** Whether or not the previous round passes, return to Stage 1 with its verdict and register the next question. Often the conclusion you carry back is only “this direction was not supported,” but it still narrows the search space for the next round.

Quantitative traders repeat these six stages. There is little room in the process for “watching the market” or “placing orders by feel”; most of the work is repeated recording, checking, and adjudication.

## Why Most Ideas Are Eliminated

Markets are nearly efficient, so the research process is naturally a filtering machine: most ideas that seem reasonable turn out to be coincidences, or too thin to cover costs. When a mature researcher sees a beautiful curve, their first reaction is not to celebrate it, but to ask: “Which test is most likely to overturn it?”

For now, remember the rhythm of research: forming an idea is quick; reaching a credible conclusion is slow; and a credible conclusion is often negative. Chapter 6 will fully explain how to turn intuition into a falsifiable hypothesis, and Chapter 15 will explain how to preserve negative results as knowledge.

So rejecting ideas is not an accidental loss in research. It is the most common output when the research cycle is working normally.

## Why Repetition and Boredom Can Be Good

The process looks repetitive because research is more like calibrating instruments in a laboratory than waiting for inspiration in front of a screen. Every idea follows the same steps; every backtest is checked for look-ahead bias, survivorship bias, and overfitting; every conclusion must state how it could be wrong.

That repetition does not guarantee an edge. It buys something more modest: a reproducible process, auditable conclusions, and less room for improvised explanations to quietly rewrite the result.

A researcher may therefore spend an entire day reading reports, debugging, or rejecting hypotheses without producing any profit, yet still increase the credibility of the conclusions. Returning to the opening example, the problem with the 115 commits was not that there was too much activity, but that the activity was not connected to an adjudicable question.

## Discipline Is Not Courage; It Is Recording Every Step

A research process makes every key decision traceable: what the original idea was, which version of the data was used, which parameters changed, which check failed, and why the final decision was to continue or stop.

Without these records, emotion does not need to cheat openly. It only has to quietly move a threshold, ignore an ugly sample, or present an exploratory finding as a prediction made in advance, and the whole conclusion becomes distorted. The point of the process is to make such changes impossible to make silently.

The discipline of a quantitative researcher can be stated concretely: **important decisions must leave an auditable trail.** Chapter 6 explains how to write hypotheses clearly; Chapter 8 explains how to lock down a test specification; Chapters 11 and 13 bring the same discipline to risk and live trading.

> **⚠️ Common Misconceptions**
>
>
> **Misconception 1: Treating “find a profitable strategy” as the only objective.** Research can also produce a credible conclusion that does not support the original hypothesis. If only positive results are preserved, researchers are more likely to beautify noise and repeat directions that have already failed.
>
>
> **Misconception 2: Measuring progress by “busyness” and volume of activity.** Changing code, watching the market, and trying parameters are all activities. When measuring research progress, ask whether those activities produced more conclusions that can be independently checked.

## 📌 Chapter Takeaways

- The core job of a quantitative trader is research, not watching the market; placing an order is only a small step at the end of the research chain.
- The research cycle has six stages: **form a hypothesis → find data → backtest → try to disprove it → risk gate → iterate**. Later chapters unpack each stage.
- Most ideas are eliminated because the filtering process is working normally; the true unit of progress is a credible conclusion, not code commits or number of actions.
- For a conclusion to be reviewable, you must retain the hypothesis, data version, parameter changes, failed checks, and rationale for the decision.
- The value of process discipline is that it prevents moving thresholds, ignoring samples, and changing your story afterward from happening quietly.

## ✍️ Try It / Think About It

1. **Draw a research cycle for one idea.** Choose any market claim, then write one line for each of the six stages: what you want to test, what data you need, how you would simulate it, where it is most likely to fail, what the risk gate asks, and how you would record the next step regardless of the result. Do not run any data yet; just check whether this chain has a broken link.
2. **Redesign your progress measure.** Think back to a recent busy workday. Delete “how many messages I sent, how much code I changed, and how many meetings I had,” and write down only the reviewable conclusions added that day. If there are none, you have not found a failure; you have found the part of the process that most needs improvement.

---

# Chapter 4: How Markets Work: Order Books and Liquidity

A trading app compresses the market into a “current price” and a “Buy” button. You press the button and receive a “Filled” notice a fraction of a second later, but the screen does not tell you who was on the other side, what queue the order passed through, or whether that price represents the last trade or the current quote.

Behind the button is the exchange's matching system. This chapter takes apart only two questions: how the market price on the screen is formed, and why an order often executes at a different price. Without understanding this mechanism, a backtest's execution assumptions may be detached from reality.

## A Market Is Not One Price; It Is a Stack of Queued Orders

Start with an everyday example. You are selling an old camera at a second-hand market and think, “At least 100 yuan,” so you list it at 100. The stall next to yours has people selling the same model: one lists it at 101, another at 102. What about buyers? One is willing to pay 99, one will only pay 98, and another calls out 97.

Arrange those intentions to sell and buy in price order, and you have an **order book**:

<table>
<thead>
<tr>
<th style="text-align: left;">Order side</th>
<th style="text-align: center;">Price (yuan)</th>
<th style="text-align: center;">Quantity (shares)</th>
<th style="text-align: left;">Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Ask</td>
<td style="text-align: center;">100.3</td>
<td style="text-align: center;">5</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Ask</td>
<td style="text-align: center;">100.2</td>
<td style="text-align: center;">3</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Ask</td>
<td style="text-align: center;">100.1</td>
<td style="text-align: center;">2</td>
<td style="text-align: left;">← Current lowest ask</td>
</tr>
<tr>
<td style="text-align: left;"><em>↕ The gap in between</em></td>
<td style="text-align: center;"><em>= spread of 0.1 yuan</em></td>
<td style="text-align: center;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Bid</td>
<td style="text-align: center;">100.0</td>
<td style="text-align: center;">4</td>
<td style="text-align: left;">← Current highest bid</td>
</tr>
<tr>
<td style="text-align: left;">Bid</td>
<td style="text-align: center;">99.9</td>
<td style="text-align: center;">6</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Bid</td>
<td style="text-align: center;">99.8</td>
<td style="text-align: center;">8</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

The top half of the table contains **asks**—the prices sellers want and how much they want to sell. The bottom half contains **bids**—the prices buyers offer and how much they want to buy. The number of shares available at each price is the **depth** at that price: it tells you how much the market can collectively absorb or supply there.

Now look at the gap in the middle: the cheapest willing seller asks 100.1, while the highest willing buyer bids 100.0. Between them is nothing—no trade. Why is there a gap? That is the subject of the next section.

## That Gap Is the Spread: The Price of Liquidity

The highest bid is 100.0, the lowest ask is 100.1, and neither side is willing to give up the 0.1 yuan in between. That gap is the **bid-ask spread**.

The spread is not a line the exchange draws at random. It is the result of buyers and sellers not yet meeting. People who keep bids and asks posted in the order book over time bear the risk of price changes and accumulated inventory; anyone who wants to trade immediately must accept the prices they offer. The spread therefore becomes the cost of being able to trade right away.

The ability to find a counterparty at any time and complete a trade at a not-too-bad price is called **liquidity**. The busier the market, the denser the orders, and the more intense the competition, the narrower the spread usually is. The quieter the market, the wider the spread.

Keep this intuition: the wider the spread and the thinner the executable depth, the higher the hidden cost of getting in and out. A neglected stock may show a “current price of 100,” while the nearest seller asks 105 and the nearest buyer offers only 95. Completing one purchase and one sale loses 10 even if the market itself does not move.

## Maker vs. Taker: Are You Providing Convenience or Using It?

The order book explains where prices come from. The next question is how orders enter it. At each match, an order takes one of two roles: providing liquidity or consuming it.

**Maker (also understood as a liquidity provider):** If an order does not immediately trade against an existing order and instead remains in the order book waiting in line, it adds liquidity at that moment. For example, if the current highest bid is 100.0 and you place a buy order at 99.9, it will not execute immediately; it will patiently join the queue. You have “added” liquidity to the market, like setting up one more stall and giving people one more choice.

**Taker (also understood as a liquidity consumer):** If an order trades against an existing order as soon as it arrives, it removes liquidity at that moment. For example, if you buy the 2 shares offered at 100.1 using an executable price, you take the goods someone else has already put on display.

**Many exchanges charge these two roles at different rates.** Makers often pay less, and some venues even offer rebates; takers usually pay more for immediate execution. The specific rules depend on the market and venue.

For a high-turnover strategy, maker or taker status can accumulate enough over time to change net returns. Chapter 10 will calculate this carefully; for now, remember: **the way an order executes is part of its cost.**

## Market Order vs. Limit Order: Do You Want Execution or Price?

Where do makers and takers come from? From the two choices you make when placing an order.

**Limit order:** You set a price boundary—“I will pay no more than 99.9; if I cannot buy at that price, forget it.” Its principle is **price boundary first, execution second**. A buy limit order will not execute above its limit price, but it may fill only partially or not at all. If the market keeps rising, your 99.9 order will sit there alone, watching the train leave. A limit order usually makes you a maker.

**Market order:** You do not specify an execution price; instead, you tell the system to complete the order as quickly as possible at the quotes available at that time. Its principle is execution first, price second. The benefit is that it will almost certainly execute; the downside is that you do not know in advance how bad the execution price may be. A market order usually makes you a taker.

Neither order type is inherently superior. A limit order protects a price boundary but may miss execution; a market order increases execution certainty but leaves price risk to the order book. Whichever you choose, you cannot avoid the next fact: liquidity is finite.

## The More You “Take,” the More the Price Moves Against You

Return to the order book. Suppose you submit a **market order to buy 5 shares**. How will the market fill it?

It starts with the cheapest asks and takes them level by level:

- First, take all 2 shares at 100.1 yuan → spend 200.2 yuan
- That level is gone, so take the next 3 shares at 100.2 yuan → spend another 300.6 yuan
- You now have 5 shares and have paid 500.8 yuan in total

Your **average execution price = 500.8 ÷ 5 = 100.16 yuan**.

The best ask on the screen was 100.1, yet the actual average price was 100.16. The extra 0.06 is not a fee; it is the result of consuming two levels of the book. This effect, in which your own order pushes the execution price against you, is called **market impact**.

The unfavorable gap between the benchmark price you chose and the actual execution price is often summarized as **slippage**. Market impact is one source of slippage; price movement while the order is transmitted, orders passing through multiple depth levels, and partial fills can also create a gap.

**Liquidity is finite.** The more urgent and larger the order, the more likely it is to consume deeper and more expensive quotes. The same order may have little effect in a market with ample depth but materially raise costs in a shallow one. We can now return to the opening question: what does the “current price” on the screen actually tell you?

## Therefore, the Price You “See” Is Never the Price You Execute At

What the large “current price of 100” in an app represents depends on the platform: it may be the last trade, the midpoint of the best bid and ask, or a mark price. It describes a quote or calculation convention; it does not promise that your order will execute at 100. What you actually face are the current best bid and ask, the quantity at each level, and the people queued ahead of you.

This has a direct implication for research: a historical closing-price series does not tell you how much could have been executed, whether you could have obtained a place in the queue, or how many depth levels a market order would have consumed. Chapter 10 will turn these mechanisms into cost and execution assumptions; for now, retain the underlying fact:

**Price must always be considered together with quantity, direction, and timing. The market does not owe you a good price, and it does not guarantee that your limit order will execute.**

> ### ⚠️ Common Misconceptions
>
>
> **Misconception 1: “My limit order is guaranteed to execute as soon as the price reaches it.”** Not necessarily. Even if the market touches your price, earlier orders may be queued ahead of yours; whether your turn comes depends on matching rules, queue position, and actual traded volume. A buy limit order means “do not execute above this price,” not “I am guaranteed to buy.”
>
>
> **Misconception 2: “If the screen shows 100, I can buy at 100.”** That 100 may be the last trade, the midpoint, or a platform mark. Whether you can execute near that price depends on how wide the spread is right now, how deep the book is, and how much you want to buy at once. With a small order in a deep market, you may pay only a little more; with a large order in a shallow market, you will personally buy the price higher level by level. The price you see is always a reference, not a promise.

## 🔬 A Lesson from Practice: The Screen Price Could Not Fill That Order

How can the mechanisms above destroy a backtest? The lab once had a curve that rose steadily and almost never looked back, and the team was preparing to advance it.

Then someone asked one more question: “How much does this instrument usually trade in a day? How much quantity was available at that price?” Once order size and order-book depth were put back into the picture, the answer was ugly: the best price could fill only a very small portion; the rest either had to keep taking worse prices or could not get a place in the queue at all.

The curve collapsed. This is an order-book lesson, not merely a cost lesson: **if there is no executable quantity beside a price, it is not a quote you can take.** From then on, research reports could not simply say “executed at what price”; they also had to say “with what quantity, using what order type, and under what queue assumption.”

## 📌 Chapter Takeaways

- A market price is not “one number,” but a stack of bids and asks queued by price, collectively called an **order book**; the quantity that can trade at each price is called **depth**.
- The gap between the highest bid and lowest ask is the **spread**, the price of liquidity; a wider spread means trading is harder and hidden costs are higher.
- A **maker** leaves an order in the book and adds liquidity; a **taker** executes immediately and removes liquidity. A maker is not necessarily a professional market maker, and fees depend on the rules of the specific market.
- A **limit order** sets the worst acceptable price and may fill partially or not at all; it can also cross the spread and become a taker. A **market order** prioritizes speedy execution, but does not guarantee a price or completion in every situation.
- The more you buy, the more levels of the order book you consume, creating **market impact** and **slippage**; your actual average price is worse than the best price you saw.
- The “price you see” is not the “price available for your execution”; research must record direction, quantity, order type, and queue assumptions, with the cost model left to Chapter 10.

## ✍️ Try It / Think About It

1. **Open any free market-data or trading app and find the “five levels” or “order book” view for an instrument** (usually near the order-entry page). Find the current best bid and best ask; subtract one from the other to get the current spread. Then compare a popular large instrument with an obscure small one: whose spread is wider? What does that difference tell you about liquidity?
2. **Do the math.** Suppose an instrument’s ask-side order book has 100 shares at 50.0 yuan, 100 shares at 50.1 yuan, and 100 shares at 50.2 yuan. If you submit a market order to buy 250 shares at once, what is your average execution price? (Hint: consume it one level at a time.) Then consider this: if you buy only 50 shares, what is the average price? The difference is the hidden cost of buying too much at once.

---

# Chapter 5: Data Is Your Lifeline: Clean Data and Look-Ahead Bias

A ship is preparing to cross unfamiliar waters. Its navigator is experienced, its hull is sound, and its route has been planned almost perfectly: avoid the reefs, follow the currents, calculate every turn. Yet one day after setting sail, it strikes a reef and sinks.

Neither the navigator nor the ship is at fault. The map is: the reefs are marked in the wrong places, and the currents point the wrong way. Once the map cannot be trusted, a carefully planned route only carries the ship faster toward disaster.

In quantitative trading, data is that map. No matter how clever your strategy, elegant your code, or rigorous your statistics, if the data you feed it are wrong, dirty, or contaminated with information you could not possibly have known at the time, then the beautiful returns you worked so hard to calculate are nothing but a mirage.

These problems do not announce themselves with red error messages, yet they can push an entire backtest away from reality. This chapter examines the risk of “the program runs normally while the conclusion is already distorted” along three lines: temporal order, historical samples, and data alignment.

## Garbage In, Garbage Out

Engineers have an old saying: “garbage in, garbage out.” It means that no matter how precise a machine is, if you put garbage in, it can only produce garbage.

A strategy merely turns input data into decisions; it does not question whether those inputs are reliable. It is like a precise machine with no capacity for doubt: one mislabelled price can travel through the entire calculation chain and emerge as a false entry and a false profit.

Validate the data before evaluating the strategy. A wrong strategy affects one idea; wrong data can contaminate every study that uses them. That is why the first class of checks asks whether the information truly existed at the time.

## The Number-One Killer: Look-Ahead Bias

One of the most common errors in temporal order is **look-ahead bias**, sometimes called using a “future function.”

Here it is in plain language: **look-ahead bias means that, at the moment you make a decision, you quietly use future information that you could not possibly have known then.**

Consider a student who claims to be able to “predict” exam scores with astonishing accuracy. You investigate and discover that they only make their “prediction” after the exam is over, the teacher has graded the papers, and the scores have been posted. Of course they are accurate—the answers are already in front of them. Such a prediction is worthless, because at the moment you place a bet in real life, the future has not happened yet.

The mistake is obvious when described aloud, but it can be hard to notice once written into backtest code, and it often throws no error. For example:

> You want to test this rule: “If a stock rises especially sharply on a given day, it will fall back the next day, so short it before today’s close.”
> But in your code, you use the day’s “high price,” which is only finalized after the close, to decide whether it rose especially sharply that day.

The problem is temporal order: you intend to place an order **before the close**, yet use the full-day high that is not finalized until **after the close**. A decision at 2 p.m. cannot depend on information that will not be complete until 4 p.m.

Look-ahead bias is frightening because it often pushes a backtest **toward a more attractive-looking result**, especially when future information directly determines selection, ranking, or execution. Of course, an error can also make results worse; the key is not that the direction is always fixed, but that the result has lost any executable meaning. When a strategy’s backtest looks too good to believe, an experienced person’s first reaction is not celebration, but: “Did I peek into the future somewhere?”

## The Point-in-Time View: Put On the Glasses of That Moment

The core defense is to maintain a **point-in-time view**: every decision may use only information that was genuinely visible at that moment.

It means: **when simulating a decision at a past moment, you may use only the data that were genuinely available to you at that moment; anything that appeared or was corrected later is off limits.**

It is like evaluating a historical figure only through “the glasses of that time,” rather than inserting later answers into the past. The principle sounds simple; the difficulty is that many data are revised after the fact:

- A company’s financial report may be corrected months later, changing the original figures.
- Government economic data are often quietly revised the following month.
- The constituent lists of some indexes are adjusted retrospectively.[^index-point-in-time]

[^index-point-in-time]: A point-in-time view must distinguish the announcement date, effective date, historical constituent list, and subsequent revisions; a constituent list downloaded today cannot directly represent the investable universe that was knowable in the past.

If a database stores only final values, a backtest may use revisions that had not yet been published at the time. A rigorous data system must also preserve the version visible at each point in time.

## Survivorship Bias: You See Only the Samples That Survived

The second major trap is **survivorship bias**. It hides in data in a particularly subtle way.

Start with a classic image. During a war, batches of aircraft go out on missions, and only some return. Someone proposes reinforcing the parts of the returning aircraft with the most bullet holes. But a clever statistician asks: you can see only the aircraft that returned. The ones hit in vital areas never made it back for inspection—so the places with the fewest bullet holes are the most lethal and most deserving of reinforcement.

Survivorship bias in data follows exactly the same logic. Suppose you want to test a stock-selection strategy, so you obtain historical data for “all stocks still in the market today” and backtest it. That sounds reasonable, right? But you have missed an entire group: companies that have delisted, gone bankrupt, been removed, or disappeared over the years.

In fast-changing markets such as cryptocurrencies, this problem is especially clear. Assets still listed on exchanges today are only part of the historical set of projects; complete data are often harder to obtain for assets that went to zero, were delisted, or lost liquidity for long periods. If you backtest using only those that are “alive,” the results will systematically omit the paths of failure.

**Clean data must define the sample according to the investable universe at the time and preserve delisted, removed, and failed members whenever possible.** The point is not to indiscriminately throw in everything that died, but to avoid passing today’s survivor list off as the opportunity set of the past.

## Alignment, Timestamps, and the Traps That Do Not Throw Errors

Look-ahead bias and survivorship bias change the content of the data. The next class of problems changes the relationships among datasets: formats, timestamps, and alignment.

A strategy often reads prices, volume, and other indicators from several exchanges at once. If one timeline shifts by even a single interval, the relationships among the data change. The most common cause is a failure to standardize **timestamps** and **time zones**.

At the same moment, some data are recorded in the time of your city, some in Greenwich Mean Time, and some simply as seconds counted from 1970. They may refer to the very same second while looking entirely different. Once you stitch together data from different time zones as if they shared one timeline, your “now” no longer matches its “now,” and a quiet form of look-ahead bias slips in—you may inadvertently use data from “eight hours in the future” to make a decision “now.”

These errors usually do not throw exceptions. The program keeps reading and calculating even though the result has departed from what was intended. In the lab, this is called **silent failure**: a fault that throws an error at least stops the process; one that stays quiet must be found proactively through coverage, time-alignment, and read-back checks.

Data APIs can also truncate silently. Historical APIs from exchanges and data providers commonly impose limits on pagination, records per request, request frequency, and how far back data can be retrieved. Without page-by-page validation, a download may stop midway while still returning a normally formatted file. You think you obtained two years of data when you may actually have only three months.

So when you receive any dataset, do not rush to use it. Ask it a few questions first: Which time zone does its time use? How long does it really cover, and are there gaps? Where did the “missing samples” go? These seemingly simple questions matter far more than whatever flashy algorithm your strategy uses.

> ### ⚠️ Common Misconceptions
>
>
> **Misconception 1: “The backtest made a fortune—I’m rich!”** A result that is too good to be true should trigger an audit first, not celebration. Look-ahead bias is only one suspect; you must also check for survivorship bias, repeated testing, incorrect execution, and program bugs. The more outrageous the curve, the more urgently you should identify which real-world constraint has been removed.
>
>
> **Misconception 2: “If the program did not throw an error, the data must be fine.”** This is the most expensive lesson for beginners. No red text does not mean everything is normal; it may only mean the error was too quiet to be caught. A wrong time zone will not throw an error, half the data missing will not throw an error, and receiving revised numbers will not throw an error. Truly clean data require active verification, not passively “waiting for it to throw an error.”

## 🔬 A Lesson from Practice: The Data That Would Never Be Seen

Our lab once learned a hard lesson from a time-zone bug.

Here is what happened. One program was responsible for downloading market data and storing them in a database for later research. Starting one day, everyone had a vague sense that something was wrong: the program ran every day, everything appeared normal, and it had never thrown an error, yet the downstream analysis could not retrieve the latest data. It was as if a batch of data had been written into a corner that no one could see.

After a long investigation, we found the culprit: an unremarkable line of time handling. When the program stored the data, it miscalculated the timestamp by a full eight hours—roughly the width of one time zone. The data themselves had been written perfectly well into the database, not a single bit missing; the program also believed it had done its duty and happily reported success.

The problem was that the program responsible for reading them later searched for data using the “correct time.” It went to retrieve data at the point called “now,” while that batch had been given the wrong label of “eight hours earlier (or later)” and lay quietly at another point in time. The two programs were like two people who arranged to meet at the same coffee shop but each remembered the wrong city—one was waiting, while the other had arrived but would never meet them. The data really existed, yet would never be seen.

The process produced no crash, red text, or warning, so the error persisted for several days. Once it was found, the lab added a check: writing data is only half the job. The data must also be read back, and their coverage and time alignment verified, before downstream research can be said to have received what it expected.

## 📌 Key Points

- **Garbage in, garbage out.** Data are the base map for a strategy; when the map is wrong, more precise calculations only make you more confident in going the wrong way. Audit the data before evaluating the strategy.
- **Look-ahead bias is the number-one killer.** It lets a decision use future information that was unknown at the time. It often makes a backtest look better, but can also distort results in other ways.
- **Maintain a point-in-time view.** Use only data genuinely available at that moment; be wary of numbers revised after the fact.
- **Survivorship bias hides in lists.** Research must sample according to the investable universe at the time and preserve members that later delisted, were removed, or failed whenever possible. Do not replace historical samples with today's survivor list.
- **Silent failures do not announce themselves.** Problems involving time zones, timestamps, data alignment, and pagination limits usually do not crash the program, so they must be verified proactively.

## ✍️ Try It / Think About It

1. **Download a free stock-price or crypto-price dataset and become a detective.** Do not rush to calculate a strategy. First spend ten minutes interrogating three questions: (1) Does the timestamp represent the start of an interval, its end, or the trade time, and which time zone is it in? (2) What date does it begin and end on, and what gaps lie between? (3) If it is cross-sectional data, does the list preserve members that had already delisted or been removed at that time? If you cannot answer, do not build a strategy on it yet.
2. **Think about it:** Suppose you design a rule: “Buy a stock when it is added to a well-known index.” For this rule to be genuinely executable, at **which point in time** must you know for certain that it will be added? If your data mark a stock as an “index constituent” from long ago (even though it was actually added later), what illusion will this create in your backtest? (Hint: recall the point-in-time view and “putting on the glasses of that moment.”)

---

# Chapter 6: From Intuition to Hypothesis: Turning “I Think” into a Falsifiable Statement

## An Afternoon Intuition

One weekend afternoon, you are watching prices on your phone. A coin falls 15% in a single day, and a thought pops into your mind:

> “After falling that much, it should bounce, right?”

The idea may be right, but the sentence is not yet testable.

How much is “falling that much”? Does a 5% drop in a day count, or must it be 15%? How much must it rise for “it should bounce” to count? Does a 0.1% rise count as a bounce? Does 3%? Which is it? And how soon must this “bounce” happen? An hour? A day? A week?

The same statement—“I think a large drop will bounce”—can be interpreted in many ways. When the definition is unclear, you can rescue the original claim no matter what the market does: a rise counts as the bounce, a further decline means “it has not fallen enough yet,” and no movement means “it is building up.”

An idea that cannot be judged wrong has no research value. This chapter turns a vague “I think” into a proposition with clear conditions that may fail to receive support.

A hypothesis is a testable proposition produced by narrowing a vague intuition. Without one, backtesting, statistics, and cost estimation have no clearly defined object. Think of it as an exam paper waiting to be graded: it is not a conclusion, but a question stated in advance and submitted to the evidence for judgment.

## “Falsifiable”: An Idea’s Admission Ticket

First, a concept that may initially sound counterintuitive: **the important thing about a good idea is not how likely it is to be right, but whether it can be wrong.**

This idea is called **falsifiability**, a concept associated with the philosopher of science Karl Popper. In other words, a claim has research value only if some possible observation would conflict with it; otherwise, no matter how the data change, they can never truly adjudicate the claim.

“Tomorrow the sun will rise in the east”—this statement is falsifiable. If an observation contradicting its definition occurs, the statement is challenged. Falsifiability qualifies a statement to be tested; not being overturned by one test does not mean it has been permanently proven.

“There is a mysterious force in the universe that we can never detect and that interacts with nothing”—this statement is **not falsifiable**. You have no way to design an experiment proving it does not exist. It may sound profound, but because it refuses every test, it is useless for your trading.

Back to markets. “This coin has great potential” is not falsifiable—what is potential? How long may it take to materialize and still count? You can always say, “Its potential has not emerged yet.” But “This coin’s average return in the first hour after the U.S. stock market opens is higher than in the other 23 hours”—that statement is falsifiable, because I can define the sample, metric, and threshold in advance; if it does not meet them, this version of the claim fails the test.

> In the world of quantitative research, “it might be wrong” is not a flaw; it is the admission ticket. An idea that can never be wrong is an idea from which you can never learn anything.

The more clearly a claim is written, the easier it is to attack with counterexamples. Only after it survives repeated tests do we have reason to raise our confidence gradually, and even then we cannot treat it as an eternal truth.

## The Four Parts of a Good Hypothesis

A usable hypothesis normally specifies four elements:

**Part one: a direction.** You must state clearly whether something rises or falls, increases or decreases. “These two things are related” is not enough; say, “When A is high, B tends to rise,” or “fall.” Without a direction, you cannot even judge right from wrong.

**Part two: measurability.** Every word in the sentence must be translatable into a number you can look up in the data. “Falls a lot” will not do; “falls more than 3% within one hour” will. “Afterward” will not do; “within the next 30 minutes” will.

**Part three: a mechanism.** In addition to stating what will happen, propose why it could happen: which participants face what constraints, and what actions might produce the expected effect? A mechanism does not prove the hypothesis, but it helps identify the environments in which the hypothesis may fail.

**Part four: it can be overturned.** Bringing the first three together, your statement must ultimately yield a clear result: “If I see X, it means I was wrong.” If you rack your brains and cannot think of an outcome that would prove you wrong, it is not because the idea is too strong; it is because it is still too vague. Go back and keep carving.

Let us run the opening sentence, “I think a big drop will bounce,” through this narrowing process:

- Original intuition: A big drop will bounce. (It has none of the four parts.)
- Add measurement: A coin falls more than 3% in one hour. (Now there is a measurable “trigger condition.”)
- Add direction and measurement: …over the following 30 minutes, the average return is positive. (Now it has direction and measurement.)
- Add a mechanism: …because sharp short-term drops are often panic selling pressure, and once that pressure is exhausted, prices repair modestly. (Now it has a why.)

It finally narrows to this statement:

> **When a coin falls more than 3% in one hour (trigger), its average return over the next 30 minutes, after costs, will exceed a pre-specified minimum threshold (direction + measurement); my mechanism hypothesis is that some sharp drops arise from temporary liquidity shortages and panic selling rather than a durable information shock.**

The same idea now has a clearly defined way to lose, and for the first time it has become a testable object of research.

## The Falsification Contract: Write Down What Would Prove Me Wrong First

Once the hypothesis is clear, you must prevent the test standard from drifting after you have seen the answer. Before confirmatory testing begins, write down the conditions under which you will concede:

> **Write down “what result would prove me wrong” before you look at the data.**

Be bold when generating ideas; once you are ready to test, however, the conditions for conceding defeat must be tightened. We call this agreement written in advance a “falsification contract.” At a minimum, it must state four things: the trigger condition, observation period, decision metric, and failure threshold.

For the sharp-drop bounce hypothesis above, the contract might read:

> I bet that after a decline of more than 3% in one hour, the average net return over the next 30 minutes will exceed a pre-specified minimum economic threshold.
> **If** the primary metric does not meet the threshold, or the estimation interval is so wide that it cannot distinguish “useful” from “not useful,” **then** this hypothesis does not pass this test. The latter should be recorded as “insufficient evidence,” not quietly substituted with “proven completely ineffective.”

The phrase “does not pass this test” limits the scope of the verdict and prevents one result from being exaggerated into a permanent judgment across all markets, periods, and parameters. Chapter 15 deals specifically with this boundary.

Why write it first? Because once you see the data, your success criteria begin to drift. If it rises 0.3%, you will think, “That still counts as a bounce”; if it takes 60 minutes to rise, you will think, “Afterward included an hour anyway.” This may not be deliberate lying, but it is enough to make any outcome look like success.

Chapter 8 will formalize this practice as **preregistration** and explain how a record of registration can prevent selective reporting when you test many variants. For now, build the most basic discipline: before examining the data, write down the conditions under which you concede defeat in full.

> ⚠️ **Common Misconception 1: Treating “proving I’m right” as research**
>
>
> The most common thing beginners do is eagerly search the data for “evidence supporting my idea.” If you browse around, you can always find a few beautiful examples of days when “a big drop did indeed bounce,” and become more excited the more you look. But this is “confirmation bias”—you see only what you want to see. Real research points in the opposite direction: actively look for “counterexamples,” asking, “When did a big drop keep falling instead?” and “What data error could create this picture?” An idea that withstands one round of attack has only earned the right to the next round of testing; it has not been proven true. Looking only for supporting cases is not research; it is self-hypnosis.

## Mechanism Hypothesis vs. Curve Fitting: There Must Be a “Why” Behind Profit

Of the four elements, mechanism is the one most often skipped. If you put enough time series into a computer, you can always find that food production somewhere and a stock index moved in close sync for a period; that co-movement alone is not enough to justify a trade.

Of course not based on this chart alone. Two curves moving together may result from a common trend, sample selection, or pure coincidence; if you cannot explain who affects whom through what channel, it lacks support for extrapolation. Looking alike numerically does not mean they are related economically.

Here we must distinguish a **mechanism hypothesis** from **curve fitting**.

- **Curve fitting** means taking a pile of historical data and repeatedly trying different rules and numbers until you assemble a line that looks spectacularly profitable in the past. You do not know why it made money; you know only that “this set of numbers happened to be very profitable in the past.”
- A **mechanism hypothesis** means you can **first** explain a rationale—that a group of market participants, for some reason, will do something at some time, and that action will predictably move prices—**then** verify in the data whether the traces of that rationale are present.

There is only one historical dataset. Try enough rules on the same data and you can always assemble one that fits the past; when moved to a new period, it often fails.

A hypothesis with a mechanism does not merely bet that “this set of numbers was accurate in the past”; it also includes the possibility that the constraints, motives, or institutions driving the phenomenon may persist in the future. A mechanism cannot guarantee the future, and a complete causal story is not necessary for every predictive model; but it can tell you why extrapolation may be warranted, under which conditions it may fail, and how to design more targeted attempts at falsification. It is an important defense against pure curve fitting.

Whenever you propose an idea, answer one question:

> “If this really can make money, what mechanism pays for the return? Does it come from bearing some risk, providing liquidity, meeting someone else’s hedging need, or taking advantage of trades that constrained participants must make?”

If you can answer—for example, “I provide liquidity to people who urgently need to exit, so I bear short-term inventory risk and receive compensation”—then you at least have a testable mechanism. The counterparty here need not be foolish; they may be meeting hedging, regulatory, funding, or time constraints. If you hesitate and can say only, “The data show it makes money,” then you need stronger out-of-sample evidence and stress testing. Chapter 9 will turn this into executable rules; Chapter 8 will address directly why overfitting can disguise historical coincidence as a pattern.

> ⚠️ **Common Misconception 2: Seeing a beautiful curve first, then inventing a story afterward**
>
>
> There is a subtler form of self-deception: you first find a profitable curve in the data, then, to convince yourself, construct a plausible-sounding mechanism story “in reverse.” This is the exact opposite of having a mechanism first and then testing it, even though both may end up looking like they “have a story and data.” The way to distinguish them is to write down the time order clearly: an ex ante mechanism can enter confirmatory testing; a story that emerges only after seeing the data can only be registered as a new exploratory hypothesis and tested on new data. An after-the-fact explanation is not necessarily wrong, but it cannot masquerade as an ex ante prediction.

## Where Hypotheses Come From: Four Kinds of Clues

However rigorously a hypothesis is written, you first need a question to ask. Common clues come from roughly four places:

**Your own observations.** The thoughts that arise while watching markets, reading news, or working with data: “It seems that every time …, … happens.” The opening idea, “a large drop will bounce,” came from observation. Such ideas are usually vague and need to be narrowed further.

**Market anomalies.** These are phenomena documented in academia and industry that appear not to fit a simple efficient-market intuition. They are clues already filtered by earlier researchers, but after becoming public they may become crowded, decay, or hold only in the market and period of the original study. A paper provides a starting point, not a guarantee.

**Market microstructure.** Mechanisms such as order books, bid-ask spreads, and the impact of large orders leave measurable behavioral traces. Chapter 4 introduced the relevant foundations.

**Other people's research.** Papers, blogs, and public strategy discussions can provide propositions to reproduce. First check whether the original result can be reproduced under the original conditions, then ask whether it still has independent justification after changing the market, data, or mechanism.

Obvious topics usually face fiercer competition. Niche topics may be constrained by capacity, data, or execution, or may contain no tradable value at all. Whatever its source, first turn the clue into a falsifiable hypothesis, then submit it to the data for judgment.

## 📌 Key Points

- **A hypothesis is the starting point of all research.** Without a testable statement, backtesting, statistics, and cost estimation have nothing to work on.
- **Falsifiability is the admission ticket.** An idea has research value only if there is some result that would make you concede defeat; an idea that is always right is worthless.
- **A good hypothesis has four parts: direction, measurability, a mechanism, and the ability to be overturned.** Carve a vague intuition into a statement along these four dimensions.
- **Write a falsification contract before confirmatory testing.** Fix the trigger, horizon, primary metric, and failure threshold; record failure to meet the threshold separately from insufficient evidence.
- **Making money should ideally have a “why.”** A mechanism cannot guarantee the future, but it can explain what risk, constraint, or service may pay for returns, and point to the conditions in which a strategy may fail.
- **Inspiration has four wells: your own observations, market anomalies, market microstructure, and other people’s research.** Different sources do not change the standard of judgment; niche and public ideas alike must face the same tests.

## ✍️ Try It / Think About It

1. **Carve a sentence.** Take a vague market intuition you believe (for example, “a stock price will rise after good news” or “high-volume stocks tend to continue their strength the next day”) and use the four parts in this chapter to rewrite it as a hypothesis with direction, measurability, a mechanism, and falsifiability. When you finish, read it aloud and ask yourself: how would the market have to move to prove me wrong? If you cannot answer, it has not been carved enough yet.
2. **Sign a contract.** For the hypothesis above, write a three-line falsification contract: first line, “What I bet”; second line, “If I see what in the data”; third line, “Then I admit I was wrong and the idea is discarded.” Then—do not rush to check the data. Simply writing these three lines clearly turns a comfortable story into a research subject that can receive a verdict.
3. **Catch a coincidence.** Think of any claim you have heard that “XX indicator is very accurate” (in the stock market or everyday life), and ask: is there a plausible mechanism behind it, or are two things merely moving together by chance? Practicing the distinction between mechanism and coincidence is a muscle you will use every day in the future.

Next chapter, we will take the hypothesis you worked so hard to carve and enter the machine that is both a time machine and a truth-revealing mirror: backtesting. You will see that the same hypothesis produces entirely different results in the hands of an honest person and a cheater.

---

# Chapter 7: Backtesting: Your Time Machine and Your Mirror

**Backtesting** is like a time machine that can only replay history: it places a clearly specified set of trading rules into past data and estimates “what would have happened if those rules had been followed under the information and execution constraints available at the time.”

Its danger is not that it lies deliberately, but that it is too obedient. Historical answers are already visible, so a researcher can easily choose entry and exit points after seeing the result, change parameters, or ignore real-world constraints. The same machine can therefore eliminate ideas that do not hold up or package the researcher's expectations into a beautiful curve. This chapter first explains what backtesting can answer, then examines how its results can be distorted.

## What Backtesting Can and Cannot Give You

First consider what it can answer, then the boundaries it cannot cross.

Backtesting's greatest value is that it compresses years of history into a repeatable check. A real human trader who wants to observe what would happen across different years by “selling when price falls below the monthly moving average and buying when it rises above it” cannot literally live through time again. A computer, however, can quickly list the number of trades, the distribution of returns, and drawdowns. It does not give you years of live trading experience; it gives you a structured record of historical counterfactuals.

That is what backtesting gives you: a **quick sieve for discarding bad ideas**. Many intuitions that seem promising will quickly reveal their problems in even the most basic historical replay. That function alone—using paper evidence to eliminate ideas that plainly do not hold up—is already valuable.

But the time machine is not a crystal ball. **A backtest describes how a rule performed in a particular history under particular assumptions; it does not promise that the future will repeat it.** Participants, institutions, liquidity, and competition all change. The same relationship may weaken, reverse, or hold only in a particular market regime.

Nor does it guarantee real execution, or that attractive numbers are free from contamination by look-ahead, selection, or implementation errors. In other words, a backtest must first show that it did not steal the answers.

The first step is to separate the timeline before and after each trade, item by item.

## Look-Ahead Bias: Align Four Times First

Chapter 5 already covered look-ahead bias in full. At the backtesting stage, do not merely ask whether your data contains future values. Break every trade into four times:

1. **Information time:** When did the raw data occur, and when was it made public?
2. **Signal time:** When could the rule first finish calculating from that information?
3. **Decision time:** When did the system decide to place an order?
4. **Execution time:** When could the order first enter the market, and at what price might it execute?

If the sequence of these four times is reversed at even one point, the backtest may gain an advantage unavailable in live trading. For example, generating a signal from the day's final closing price while assuming execution at that same closing price—unless you have a clearly defined closing-auction process, information cutoff, and execution model—crams “knowing the answer” and “trading on the answer” into the same instant.

For earnings reports, index constituents, and macroeconomic data, also examine the **release time or version time**. A quarter's reference date is not its publication date, and a revised value available today was not necessarily visible at the time. When auditing a backtest, answer this question for every trade: “Before this order was sent, could the strategy really have obtained this information?”

> **⚠️ Common Misconception**
>
>
> **“If the code does not reference the next row of data, there is no look-ahead bias.”** Wrong. Publication times, time zones, aggregation windows, signal-calculation delays, and execution timing can all make the data in the same row unavailable at that time. The absence of forward indexing in an array does not mean economic time is aligned.

## In-Sample and Out-of-Sample: Do Not Write and Grade the Same Exam

Strategy development and strategy evaluation cannot use the same stretch of data forever. Every time you inspect a result or adjust a parameter, that data participates in the design. If you then use it to grade the strategy, the score will naturally be too optimistic.

Quantitative research typically divides data into two categories:

- **In-sample:** the practice exam used to explore, debug, and form the rules.
- **Out-of-sample:** the final exam that does not take part in this round of adjustments and is used to estimate how the rule performs in a new period.

Financial data has a time order, so you cannot randomly shuffle it and let future observations leak into the past. Common approaches split it by time, or repeatedly simulate “train only on data available up to that point, then test forward” with rolling or walk-forward methods.

Out-of-sample data is not a magic seal. If a strategy looks good only in-sample and fails in a period that did not participate in its design, overfitting is a prime suspect. But one out-of-sample failure may also result from a changing market regime, too short a sample, or execution differences. Conversely, passing once does not mean it will work forever.

Out-of-sample data can be used up, too. Once you see its results and go back to modify the strategy, it has participated in the design. Using the same period again as a “brand-new final exam” does not restore its original role just because you keep the name.

## Costs Must Enter from the First Backtest

Chapter 4 already discussed spreads, market depth, market impact, and slippage; Chapter 10 will build a full cost model. This chapter leaves you with only one audit principle: **do not first test a world of free trading and then treat costs as a final seasoning.**

From the first version of the results, use executable buy and sell directions, estimated fees, and slippage, and check how sensitive performance is to the cost assumptions. If a slight increase in costs immediately turns net returns negative, the strategy's edge is not robust.

Also avoid a common shortcut: applying the same fixed cost to every trade. Real costs vary with the instrument, time of day, order size, maker/taker status, and market volatility. The model may start simple, but it must state clearly what it omits and stress-test worse scenarios.

> **⚠️ Common Misconception**
>
>
> **“First see whether there is alpha; deal with costs later.”** Costs change whether a signal is tradable. They are not an accounting item deducted at the end. Ignore them, and you are studying a nonexistent market with free trading.

## A Backtest Is Only a Coarse Filter, Not a Decree

Suppose you have avoided look-ahead bias, separated in-sample and out-of-sample data, and included costs. Can you go live now? Not yet. A backtest is suited only to answering, “Is this idea worth advancing to the next stage?” Historical data rarely reconstruct queue position, network latency, rejected orders, system failures, sudden liquidity drops, and market impact at real scale in full.

So a green light from a backtest means only that the idea has not been rejected on paper. It must still go through paper trading, very small live trading, and gradual scaling, aligning model assumptions with reality one by one. Chapter 13 will cover this deployment ladder in full.

A backtest is therefore a coarse screen, not the final authorization. It can reject ideas that clearly do not hold up, but it cannot sign on behalf of the real environment.

## 🔬 A Lesson from Practice: The Test Suite That “All Passed”

For a while, our lab was refining a backtesting system.

The same boundary applies to the testing system itself. One day, the person responsible ran the full automated test suite and saw an entire row of green lights without a single red mark. He nearly signed off on that basis.

But an old team rule saved us. It says: **all tests passing does not mean the program did the right thing—it may simply have done nothing at all.**

The team then asked: did these tests verify the required business behavior, or merely verify that the program did not throw an error? An empty shell that does nothing can also avoid errors and let every test pass.

We call this phenomenon “false green”: the green light is false, and so is the sense of safety.

They therefore fed the system dirty data that should have been rejected, including scrambled timestamps and missing required fields, and checked whether it failed at the intended points.

Some bad records still passed through. The original tests had not covered those failure paths, so the green lights meant only that “the covered paths did not throw errors,” not that the system had done what it was supposed to do.

**Real validation is not confirming that “it succeeds when it should succeed”; it is confirming that “it truly fails when it should fail.”**

A system that never tells you “no” is not reliable; it is frightening. It merely saves every problem for the day you use real money, when they all come due at once. This kind of negative test becomes formal governance in Chapter 13: when a critical check is unclear, the system should stop and refuse to proceed rather than carry uncertainty into real-money trading.

## 📌 Chapter Takeaways

- **Backtesting is a time machine, not a crystal ball.** It tells you how a rule performed in the past; it never promises the future will repeat it. Its greatest value is helping you quickly discard bad ideas.
- **Look-ahead bias requires a time audit.** Information, signal, decision, execution, and release times must be ordered according to economic reality. Even if the code does not reference the next row, it may still be peeking into the future.
- **In-sample data is for development; out-of-sample data estimates generalization.** Financial data should respect time order. Once an out-of-sample period has participated in revisions, it is no longer a brand-new final exam, and passing once is not permanent proof.
- **Costs belong in the first backtest.** The model may start simple, but it must state omissions and stress-test worse cost scenarios.
- **A backtest is only a coarse filter, not permission to deploy.** A green light means only “worth advancing to the next stage”; real execution still needs paper trading and small live runs.
- **Beware of “false green.”** Passing every test does not mean the system did the right thing; it may have done nothing. Real validation confirms that the system truly fails when it should fail.

## ✍️ Try It / Think About It

1. **Check for look-ahead bias.** Pick a simple trading idea you have heard or considered—for example, “buy after three consecutive down days.” Before you backtest it, write down on paper exactly what information you could and could not have at the moment of making the decision. Circle the things you could not have but would really like to use—that is where look-ahead bias is most likely to hide.
2. **Design a test that fails.** Create an order for your backtesting system with a scrambled timestamp, a missing price, or an impossible execution. First write down at which stage it should be rejected, then actually run it. If the system still shows green lights all the way through, you have not found a good strategy; you have found a false green light.

---

# Chapter 8: Statistical Rigor: Why Your “Holy Grail” Is Probably Noise

## A Fraud Who Can Call Ten Tosses in a Row

In Chapter 2's experiment with ten thousand coin tossers, a few people will always remain after ten rounds having called every toss correctly. If the camera shows only one of them, that person appears to possess a special method; put all participants back into the frame, and the apparent genius is simply an extreme value that normally appears in a large sample.

Quantitative research can build the same room: many strategies are tested, but only the best one is presented. The first step in statistical rigor is to pull the camera back and return failed versions, parameter variants, and conditional slices to the ledger. This chapter examines why an attractive equity curve may come from noise and how the selection process can be brought back into the evidence.

## Randomness Can Grow Attractive Curves Too

In a first backtest, an equity curve rising from lower left to upper right can be highly persuasive because it compresses random fluctuations into what looks like a complete story of making money.

Open a random-number tool and simulate 1,000 coin tosses: assign +1 to heads and −1 to tails, then plot the cumulative result.

A purely random path will often contain climbs, drawdowns, rebounds, and new highs. Its shape can look like a profitable strategy even though it has no predictive mechanism at all.

**An upward curve by itself proves almost nothing.** A rule with no real edge can look good through sampling luck; a valuable strategy can look bad because the sample is short, because it is used for hedging, or because it encountered an unfavorable environment. A curve must be interpreted together with the hypothesis, sample, costs, and benchmark.

The next step, then, is not to keep admiring the curve but to ask whether it comes from an explainable edge, sampling luck, the selection process, or an implementation error. The first risk is that the model memorized the answers in this particular history.

## Overfitting: Memorizing the Answers Is Not Learning

Let us start with a situation you and I have both experienced. Before an exam, you discover that the teacher will use questions from an old problem set. So you memorize every answer perfectly, score 98 on the practice test, and are ecstatic, thinking you have mastered the subject. Then the real exam uses new questions, and you score only 40.

That is **overfitting**: you did not learn “how to solve the problems”; you merely memorized “the answers to this particular test.”

In quantitative work, overfitting looks like this: you have a strategy with a parameter, say the number of days in a moving average. You do not know how many days to use, so you test 5 days, 6 days, 7 days ... all the way to 200 days, and see which produces the most profit on historical data. In the end, you find that the 43-day curve looks best, so you say: that is it—43 days.

This is not independent strategy design; it is choosing a parameter after seeing the historical result. Forty-three days may look best only because it fits the coincidences and noise in this period most closely. Move to a new period and the apparent edge may disappear.

A rough but useful intuition: **the more knobs you can freely adjust, the greater the model's ability to cling to historical noise.** This does not mean complex models are necessarily bad. It means complexity must be paid for with more data, regularization, stable out-of-sample performance, and clear incremental value. Simple is not automatically correct; it merely makes the choice space smaller and auditing easier.

That is why our lab's confirmatory specifications have an old-fashioned rule: **for every registered experiment, parameters must be specified as fixed values; you cannot hide a string of candidate values.** During exploration, you may certainly compare 5 through 200 days, but every attempt must enter the ledger and be confirmed on new data that did not participate in selection. You cannot run 196 versions, submit only the best one, and pretend you knew from the beginning that 43 was the answer.

## Multiple Testing: Try a Hundred Times and Some Results Will Be “Significant”

Return to the room of coin tossers at the beginning. Now you understand: the more participants there are, the less surprising extremely lucky ones become.

In quantitative research, the “people” are the “strategies you tested.”

Suppose you write 100 different strategies and backtest them. Statistical tests commonly use a 5% significance level: when the null hypothesis is true and the test conditions hold, a single test has about a 5% long-run chance of crossing the threshold by mistake.

If none of the 100 strategies has a real effect, then under this simplified setup about five will still cross the threshold by luck on average. Reporting only those five hides the other 95 attempts that produced them.

This trap is called **multiple testing**. The broader behavior is **data snooping**: repeatedly inspecting the same data, changing conditions in response to results, and retaining only the best version.

Data snooping is often not deliberate cheating. Each “try one more variant,” “add one condition,” or “use a different period” expands the selection space. If those attempts are not recorded, a researcher can sincerely mistake noise for alpha.

## Conditional Returns Are Also Tests

Conditional slicing is one of the most common forms of data snooping: when the overall result is unremarkable, the researcher starts looking for a version that “works only at certain times.”

You run a strategy and its overall results are unremarkable. But you cannot let it go, so you begin “slicing the data”:

“What if I trade only on Mondays?”—it seems a little better.

“What if I trade only when volume expands?”—hey, a little better again.

“What if I trade only before 10 a.m., and only when the previous day closed down?”—wow, the curve becomes gorgeous!

Excitedly, you announce: I found it! This strategy is unbeatable on “Mondays + rising volume + before 10 a.m. + yesterday closed down”!

Stop. Every “only when...” adds another researcher degree of freedom and another opportunity to select an accidental winner. These slices are often highly correlated, so you cannot simply treat them as independent; but correlation does not make them free. If you tried dozens of conditions on the same data and report only the best one, the statistical evidence is still contaminated by the selection process.

**Conditional returns must enter the attempt record for the same research family.** Record which slices you tried, in what order, and under what selection rule. The finer the slicing and the brighter the result, the more you need new data and evidence of a mechanism.

## Write Down What Would Prove You Wrong First: Preregistration

Exploration is allowed to try things. The issue is not trying, but whether the complete record is preserved afterward and whether exploration is kept separate from confirmation. A common practice is **preregistration**.

The concept is almost plain in its simplicity: **before beginning a round of confirmatory testing, write down and register the hypothesis to be tested, strategy specification, primary metrics, and decision rules.** You may of course have explored old data already; the key is to label new ideas honestly as exploration, then confirm them using data that did not participate in selection. You cannot disguise exploratory results as predictions made in advance.

When the “Mondays + rising volume” curve looks especially attractive, people can easily invent a plausible story after the fact and misremember it as what they had predicted all along.

This is hindsight bias. If the preregistered hypothesis said “the strategy should work on all trading days,” but it later performs better only on Mondays, the Monday condition must be labelled a new exploratory finding. It cannot be rewritten as the original prediction.

Chapter 6's falsification contract answers “What am I betting on, and what counts as losing?” Preregistration goes one step further: it leaves a time-stamped record of the specification that can be checked, and explicitly labels variants created later as new experiments. Exploration remains free, but reporting cannot selectively forget.

> ### 🔬 A Lesson from Practice: Put a Lock on Your Future Self
>
>
> In our lab, a confirmatory test begins only after the complete specification has been written down: what is being tested, the parameter values, what counts as passing, and what counts as a lack of support. The record is then “registered on-chain.”
>
>
> “On-chain” is not the important part. Any append-only record that reliably preserves a content hash, version, and timestamp can serve a similar purpose.
>
>
> Some people regard the procedure as a waste of time and believe they will remember the original specification.
>
>
> In practice, when strategy A is unremarkable but a later slice, variant A', looks excellent, people can easily remember A' as the original research target. The registration record restores the actual order of events.
>
>
> Preregistration preserves the ex ante commitment so that an ex post explanation cannot masquerade as an ex ante prediction.

## Discounting Performance by “How Many Times You Tried”: The Intuition Behind DSR

Preregistration preserves “what was tried,” but the best result selected from 100 attempts raises another question: how much was the number inflated by the selection process itself?

Let us first discuss a common scorecard: the **Sharpe ratio**. In simplified terms, it divides average excess return by return volatility, measuring how much average return corresponds to each unit of volatility. The higher it is, the more favorable historical returns have been relative to volatility. But serial correlation, non-normal tails, short samples, and ex post selection can inflate it, so it cannot decide a strategy on its own.

A strategy with a Sharpe ratio of 2.0 is not evidence of the same strength as the highest Sharpe ratio selected from 1,000 candidates. The more attempts there are, the more likely the best score has been lifted by luck.

One related correction is the **Deflated Sharpe Ratio (DSR)**.

We will not expand its formula here, but you must understand the intuition:

> **For the same Sharpe ratio, the evidence is weaker if it was selected from more attempts.**[^dsr-selection]

[^dsr-selection]: A Sharpe ratio of 2.0 selected after trying 5 strategies is not evidence of the same strength as a Sharpe ratio of 2.0 selected after trying 5,000. DSR also considers sample length, skewness, kurtosis, and the effective number of independent trials.

DSR does not simply divide the Sharpe ratio by the “number of trials.” It also considers sample length, skewness and kurtosis of the return distribution, and the effective number of independent trials implied by correlations among a group of attempts. It then asks: does this Sharpe ratio still exceed the best result that data mining itself could reasonably produce?

Therefore, conditional returns, parameter variants, and filters added later must all be recorded in the ledger for the same **research family**. If attempts are omitted, any correction will be too optimistic. We would rather let an attractive number slim down early than let it carry selection bias into live trading.

## Why This Discipline Is Worth Keeping

These disciplines are not meant to prohibit exploration. They expose the degrees of freedom created by exploration so that the same evidence cannot be repackaged repeatedly as multiple discoveries.

Preregistration, research families, and DSR will not create a signal for you. What they reduce are false positives, while helping you distinguish advance predictions, post hoc exploration, and independent confirmation.

This book does not cover the formula or software implementation of DSR. For beginners, what matters more is recording every attempt in the same research ledger and asking, before interpreting the best result: if all the failed versions and the number of selections are put back into the frame, how much evidence remains?

> ### ⚠️ Common Misconceptions
>
>
> **Misconception 1: “The curve is so beautiful; it must be a good strategy.”** Even purely random coins can produce a lovely upward slope. A good-looking curve is, at most, a clue—not a pass. The real question is “Why does it look good?” not “How good does it look?”
>
>
> **Misconception 2: “I did not cheat. I just tried a few more variants and sliced the conditions a few more ways.”** This is the gentlest and most deadly form of self-deception. You are not cheating; you are data snooping—every “let me try again” puts another coin tosser into the room. Not doing it intentionally does not mean it did not happen; not blushing does not mean you did not deceive yourself.

## 📌 Chapter Takeaways

- **Randomness can grow attractive curves too.** An upward curve is a clue, not proof; it may come from a genuine edge, or from sampling luck, selection bias, or omitted constraints.
- **Overfitting is memorizing the answers.** The more adjustable degrees of freedom you have, the more you need data, regularization, and independent validation. Exploration may compare parameters, but confirmatory specifications must be fixed and all attempts must be recorded.
- **Try a hundred times and some results will be “significant.”** This is the trap of multiple testing and data snooping: the more you try, the more likely an attractive result is merely luck.
- **Conditional returns consume evidence too.** Different slices may not be independent, but they all add selection freedom; they must be included in the same research family and confirmed on new data.
- **Preregistration makes advance commitments checkable.** Record the original specification, later variants, and the number of attempts separately, so you cannot report only the prettiest version.
- **DSR corrects a selected Sharpe ratio.** The more attempts, the shorter the sample, and the less ideal the return distribution, the more cautious you should be about the best result.

## ✍️ Try It / Think About It

1. **Toss your own “Holy Grail.”** Find any tool that can generate random numbers—a phone calculator or spreadsheet will do—and simulate 200 coin tosses: record +1 for heads and −1 for tails, then cumulatively add the numbers and plot a line. Draw several lines. See how quickly you can “happen” to create an attractive curve that looks like a “profitable strategy” to an outsider. Once you have drawn one, say to it: you are just a coin.
2. **Count the people in your own room.** Under the simplified case in which the tests are independent and all null hypotheses are true, if you test 50 strategies, each at a 5% significance level, how many results would falsely cross the threshold on average? After calculating, consider this: how should you record the research family so you do not mistake one false winner for a discovery?

---

# Chapter 9: Signals and Factors—How an Idea Becomes a Tradable Rule

Chapter 6 turned vague intuition into a falsifiable hypothesis, but a hypothesis does not place orders by itself. If you put an assistant in charge of your account and say only “Buy when it looks cheap,” they still do not know how cheap, how much to buy, when to sell, or when to stop.

A machine cannot guess either. It needs explicit inputs, thresholds, position sizes, exits, and stopping conditions. This chapter explains how to translate a hypothesis into an executable rule and how to account for the freedom introduced by every parameter in that translation.

## Signals: A Light That Shows Only Three Colors

First, define a **signal**.

The simplest signal can call for one of three actions: go long (bet it will rise), go short (bet it will fall), or do nothing. But a signal can also be a continuous score—for example, directional strength from −1 to +1, or relative rankings across a basket of stocks—which a position-sizing rule then translates into action.

A traffic light is a useful analogy: green means go, red means stop, and yellow means wait—except that some lights also have a brightness level. A signal compresses a large amount of price, volume, or fundamental data into a judgment a machine can use; the strategy then combines it with position, risk, and execution rules to decide which button to press.

## Factors: The Numbers That Feed the Light

So what does this light look at? Broadly speaking, it looks at **features**, sometimes also called factors: any input that is observable and computable at the decision point, such as returns over the past five days, relative trading volume, or the bid-ask spread.

In finance, a **factor** often has a more specific meaning: it may be a systematic driver that explains common returns and risks across a group of assets, or a style measure used to rank stocks. In everyday discussion, the two terms are often used interchangeably. For readability, this book will continue to use “factor” as its main term, but remember: not every model input automatically qualifies as a validated financial factor.

Factors or features provide inputs; a signal compresses them into a direction or score.

## From One Hypothesis to a Rule with Knobs

Let us walk through a concrete hypothesis from start to finish: “If something has fallen sharply recently, it will rebound a little in the short term.”

To turn this into a machine-executable rule, we need to answer each of these questions:

- How recent is “recent”?—Say, the past 5 days.
- How sharp is “fallen sharply”?—Say, more than 10%.
- How long is “short term”?—Say, hold for 3 days after buying.

That gives us an initial rule: **If, after the close, an asset is confirmed to have fallen more than 10% cumulatively over the previous 5 trading days, enter at the next tradable opportunity using a predetermined order method, then exit after holding for 3 trading days.**

Now count the knobs hidden in this seemingly simple rule: 5 days, 10%, 3 days, plus the trading time and order method. These preset numbers and choices are called **parameters**. A genuinely live-tradable strategy must also specify the asset universe, position size, costs, signal conflicts, and exception handling; for now, we will focus on parameter selection.

## Every Extra Knob Adds a Degree of Freedom

Chapter 8 already covered overfitting. At the rule-design stage, we will focus on its most concrete source: **degrees of freedom**.

Five days, 10%, and a 3-day holding period: every parameter gives the researcher one more choice. Parameters are not inherently bad; the problem is whether, after seeing the results, you select the prettiest outcome from many candidate values and report only that final number. The more degrees of freedom you have, the faster the number of combinations grows—and the larger the statistical bill becomes.

So before adding a new parameter, ask two questions: What mechanism does it correspond to? Without it, what necessary capability would the strategy lose? If you cannot answer, do not install that knob yet.

## Robustness Checks: Do the Neighbors of a Good Parameter Hold Up Too?

To distinguish a parameter value that has a real rationale from one that merely got lucky, check whether nearby values also hold up.

A good recipe works like this: add a pinch more or less salt, and the dish still tastes good. Only then does it deserve to be called a recipe. If a “recipe” requires exactly 3.7 grams of salt, and 3.6 or 3.8 grams makes the dish terrible, then what you have is not a recipe at all—it is a coincidence that happened to work once.

Parameters are the same. If your rule works for “the past 5 days” but performs terribly at 4 days and 6 days, that is a strong warning sign: you may have landed precisely on historical noise. Smoothness in the neighborhood is not a law of nature—some regulatory thresholds or expiration dates genuinely create sharp boundaries—but if the mechanism does not explain such a discontinuity, an isolated spike is especially suspicious. We call a parameter that collapses when moved slightly **fragile**. In research, we would rather have a blunt rule that remains acceptable when it is slightly off than a miraculous rule that must be exact to the last decimal. This test is called a **robustness check**: do not look only at the instant when the light turns on; see whether the neighbors on either side can stand too.

## Ablation and Controls: Is the Mechanism Making Money, or Is It Luck?

Another check is an **ablation**.

The name sounds intimidating, but the idea is simple: remove one component of the strategy and see whether it falls apart. It is exactly like a chef asking, “Is that secret seasoning really what makes this soup taste better?” The most direct way to find out is to cook a pot without it and compare.

Suppose a strategy has three conditions: the size of the price decline, trading volume, and time period. An ablation can remove each one in turn and rerun the strategy using comparable risk, number of trades, and sample. If removing volume barely changes the performance or behavior, it may merely be decoration. But check interactions too—some components contribute little alone yet become useful in combination. Ablation is diagnosis, not a mechanical rule to delete a component whenever a number gets smaller.

Paired with ablation is a **control** or **benchmark**. A benchmark should not be an arbitrarily weak opponent; it should match market exposure, risk, turnover, or holding period as closely as possible. For example, a trend strategy can be compared with risk-matched buy-and-hold and a simple trend rule; a stock-selection factor can be compared with portfolios adjusted for market, industry, and style exposures. Together, ablation and controls ask: What did the added complexity actually contribute, and did it merely repackage a favorable market tailwind as intelligence?

## Why “Simple First” Is a Virtue

After neighborhood, ablation, and benchmark checks, why still prefer simplicity? Because simple rules are usually easier to audit, explain, and maintain. Fewer knobs mean a smaller choice space; shorter rules make it easier to locate the cause when they fail. But simple does not automatically beat complex: a complex model may deserve to exist if it consistently provides incremental value under rigorous out-of-sample, cost, and stress testing. **Every unit of complexity must explain what it buys and come with corresponding monitoring and failure boundaries.**

> **⚠️ Common Pitfalls**
>
>
> **Pitfall 1: Making parameters “optimal.”** The best-performing parameter in the historical sample fits that sample most closely and may also fit its random fluctuations most closely. If nearby values deteriorate sharply and no mechanism explains the discontinuity, the result is suspect.
>
>
> **Pitfall 2: Believing that adding more conditions or factors automatically makes a strategy stronger.** The more conditions you add, the faster the number of combinations grows. Unless every condition has an ex ante mechanism, an independent contribution, and out-of-sample evidence, complexity first increases selection bias, not edge.
>
>
> **🔬 A Lesson from Practice: The Field That Allows Only One Number**
>
>
> In our lab, we have a rule that may seem stingy: for every parameter field in a submitted strategy, the researcher may enter only one number.
>
>
> Why be so picky? Once, a researcher submitted a strategy whose “holding days” field said: “3, 5, 7, or 10 days are all fine.” He thought he was being thoughtful—leaving us flexibility to choose whichever looked best.
>
>
> “All are fine” is not one specification; it is four candidate versions. If all four have been run, they must be accounted for as four attempts. If only one is to be tested, one number must be fixed before the run.
>
>
> So the rule became: enter 3, and it is 3. Studying 5 days is fine, but it must be registered as a new variant and retested; you cannot quietly rename the original specification afterward. A seemingly stingy field protects the boundary of the experiment.

## 📌 Key Takeaways

- A signal compresses information into a direction, ranking, or continuous score. Features are model inputs, while factors often refer to features with economic meaning or explanatory power for common risk; they are not exactly the same thing.
- Every adjustable parameter expands the choice space. Parameters are not bad, but they need a mechanism, an experiment ledger, and out-of-sample evidence.
- The “neighbors” of a good parameter should hold up too: a miraculous rule that collapses when moved slightly probably just hit a lucky point.
- Ablation and controls measure the incremental value of added components. Comparisons should match risk and exposure and account for interactions between components.
- A confirmatory specification must state one fixed value. Exploring several candidates is fine, but every variant must enter the research ledger; you cannot report only the winner.
- Simple first is an auditing principle, not dogma. Complexity should not remain unless independent evidence and genuine incremental value can pay for it.

## ✍️ Try It / Think About It

1. Choose a trading saying you have heard (for example, “buy when the golden cross appears”) and identify every hidden knob: Which two moving averages? How many days for each? How long after the crossover do you enter? How long do you hold, and when do you exit? After counting, you will probably be surprised—such a simple saying hides more than one parameter.
2. Suppose someone brings you a strategy with an impressive backtest and asks you to partner with them, but you can ask only three questions to tell whether it has real skill or merely memorized the answers. Which three would you ask? (Hint: consider “Are the parameter neighbors robust?”, “Does it collapse when a component is removed?”, and “How were these parameters chosen in the first place?”)

Chapter 7 already explained how backtests can mislead you; the next chapter will calculate trading costs separately. For this chapter, hold on to one conclusion: **every knob is a place where you may deceive yourself.**

---

# Chapter 10: Execution Isn't Cheap—Transaction Costs and Conservative Fill Assumptions

A researcher turned their screen toward me. The curve climbed steadily from the lower left to the upper right, tripling over five years with only modest drawdowns. They were ready to start a small live-money trial.

I asked only one question: “How many round trips does this strategy make in a day?”

The answer was five or six. Once we added the commission, spread, and slippage that each trip should pay, the once-beautiful equity curve did not merely fail to double—it fell below the initial capital.

The signal may not have had zero predictive power. More likely, its gross edge was so thin that it could not pay for execution. Chapter 4 explained how these frictions arise from the order book; this chapter turns them into a bill you cannot avoid.

## Costs Are More Than Commissions

Transaction costs have at least three components.

**Commissions and fees.** Brokers, exchanges, or clearing services charge a fixed amount, a percentage of trade value, or a tiered rate. Some markets also distinguish between liquidity providers (makers) and liquidity takers (takers), with different fees. This is usually the easiest cost to identify, but it is not the whole cost.

**The bid-ask spread.** At the same foreign-exchange counter, the price charged to sell you currency is higher than the price paid to buy it back. Markets work the same way. If you demand immediate execution, you usually buy at the ask and sell at the bid; even if the price does not move, a buy and a sell may lose a spread immediately.

**Slippage, part of which comes from market impact.** Slippage is the unfavorable difference between the actual execution price and a benchmark price selected in advance. Network latency, changing quotes, partial fills, and insufficient order-book depth can all cause it. If the order itself consumes multiple quote levels and moves the price, that portion is **market impact**. A limit order that never fills because it cannot reach the front of the queue is more accurately recorded as a non-fill and opportunity cost.

Commissions usually appear on an explicit bill; spreads and slippage are embedded in the execution price. Different markets may also involve taxes, stock-borrow fees, funding rates, financing costs, and infrastructure expenses. A cost model can be built in layers, but the first three items must not be mistaken for the entire cost.

## Turnover: Costs Accumulate with Trading Size

Now for a key term: **turnover**. It is not simply the number of orders placed; it measures how large the traded amount is relative to the portfolio size over a period. Ten very small adjustments in a day may have lower turnover than one complete reversal of the portfolio; what really determines cost is how much you trade, in which market, and how you execute.

Costs therefore resemble a charge based on “traded value and liquidity consumed.” The higher the turnover, the more often spreads, commissions, and market impact are paid; the thinner the strategy’s edge, the less it can withstand this friction.

Let us calculate an understandable example. Suppose the strategy uses the same trade value each time, takes the mid-price as a common benchmark, and has a gross edge of about 0.10%. On one round trip, total commission is 0.05%, the cost of crossing the spread is 0.06%, and additional slippage beyond the spread is estimated at 0.04%, for a total cost of 0.15%. The benchmark is stated explicitly here to avoid counting the spread both inside slippage and separately, and deducting it twice.

A 0.10% gross edge against 0.15% costs on the same basis gives a net result of about −0.05%. If the notional amount differs across trades, you cannot simply count the number of “trips”; you must weight by the actual traded amount of each trade. This strategy might look excellent on a backtest chart because that chart depicts a world “before costs.” Once it touches real money, it begins bleeding quietly.

That was the problem with the strategy at the start of the chapter. Its signal may indeed have had a small edge, but it was too thin to support the diligence of five or six round trips a day. Costs do not need to defeat your insight; they only need to be a little thicker than your tiny edge.

A low-turnover strategy and a high-turnover strategy earning thin spreads have very different sensitivities to cost. Without a complete cost model, the latter's reported returns may be impossible to realize.

## Gross Return and Net Return: Only One Reaches Your Pocket

The figures above describe each round trip. When they flow into the full performance curve, two terms must still be distinguished:

**Gross return** is what the strategy earns “on paper” before costs—pretending that trading costs nothing.

**Net return** is what actually remains in your pocket after commissions, spreads, and slippage have all been deducted.

If backtesting software is not configured correctly for costs, its attractive curve may show only gross return. Gross return is the menu price; net return is the money actually left after paying the bill. Whether a strategy is tradable must be judged by the latter.

## Conservative Fill Assumptions: Plan for Adverse Execution

So in a backtest, what price should you assume you can execute at?

Using the midpoint between bid and ask, or the closing price, directly as an execution price is usually too optimistic. Real orders may cross the spread, wait in a queue, or consume multiple quote levels. The average buy price will be higher and the average sell price lower.

So the lab uses a **conservative execution model**: the baseline scenario estimates costs from the observable spread at the time, order direction, maker or taker status, expected size, and historical execution distributions; it then adds adverse and stress scenarios. A buy cannot assume it receives a favorable price available only to sellers, and a sell cannot assume it always fills at the high.

This does not mean casually inflating a fixed percentage, nor choosing a physically near-impossible “worst price in the universe” to torture the strategy. Excessive pessimism can also produce false conclusions. The key is that every layer of assumptions can be explained and calibrated, then continuously reconciled against real small-scale executions.

Next, perform **sensitivity analysis**: as costs are raised step by step from the baseline to adverse and then stress scenarios, how does net return change? If it turns negative with only a slight deterioration, the edge is fragile; if it fails only under an extreme, unsupported penalty, you should not dismiss it carelessly on that basis.

Only a strategy that still holds up under pre-specified, realistic, explainable adverse scenarios deserves to move to the next stage.

## 🔬 A Lesson from Practice

Once, we had a signal that looked quite ordinary. In its first backtest, using somewhat lenient execution assumptions, its returns were fairly good, and some people on the team were already excited.

But we did not rush to celebrate. Instead, we tightened the execution assumptions according to a ladder written in advance: from median historical cost to a worse percentile, then to a stress scenario; both buys and sells used quotes consistent with order direction, and slippage increased with size and volatility. We were not simply picking the single worst trade; this was a conservative range that the data could explain.

Many signals cannot withstand this treatment. Once the numbers are tightened, their previously positive returns are instantly pressed below zero—which means their apparent “profit” was really earned from our optimism about costs, not from genuine skill.

But this signal was different. Under a pre-specified stress scenario supported by the historical distribution of executions, it still retained a small positive number in our internal scoring system at the time: +0.66. That number is not a universal threshold, nor does it guarantee future returns; it merely says that this stress test had not yet pushed the result below zero, so it was worth further validation.

That internal score, still positive after being reduced, deserved further investigation more than the attractive but fragile large number in the first backtest. A stress test is not looking for a strategy that never shrinks; it is looking for one that still has room to breathe when an adverse scenario arrives.

## ⚠️ Common Pitfalls

> **Pitfall 1: Treating the closing price or mid-price as a promise of free execution.**
> The mid-price can be a benchmark for measuring execution deviation, and the closing price may be a genuine execution benchmark through a closing auction. The question is whether the strategy had a signal before the cutoff, participated in the relevant auction, and could be accommodated by the available trading volume. Assuming a full fill at the benchmark price without an execution path is what creates that imaginary accommodating market.
>
>
> **Pitfall 2: Counting only commission while ignoring spread and slippage.**
> Commission is the most straightforward and easiest-to-calculate of the three brothers, so beginners often count only it and think the cost calculation is finished. But the two brothers that do not appear on the bill are often the ones that truly drain high-turnover strategies. Invisible does not mean nonexistent; they simply do not give you a receipt.

## 📌 Key Takeaways

- Transaction costs have at least three parts: commission, bid-ask spread, and slippage; market impact is the portion of slippage caused by your own order.
- Costs accumulate with traded value and liquidity consumed: the higher the turnover, the more easily spreads, commissions, and impact repeatedly eat away at a thin edge.
- Only net return, after costs, reaches your pocket; gross return is merely the menu price before the bill is paid.
- A conservative execution model needs an explainable baseline plus adverse and stress scenarios. Do not assume favorable prices, but do not substitute baseless extreme penalties for modeling either.
- A cost model should avoid double counting and be continuously calibrated against small-scale live trading. If it remains non-negative under pre-specified stress, it deserves to move to the next stage, but that is still not a guarantee of live performance.

## ✍️ Try It / Think About It

1. Find a strategy you have “heard is highly profitable” and estimate its annual **one-way turnover**. For example, if the year’s cumulative purchases and sales equal 40 times the average capital, and the all-in one-way cost per dollar traded is 0.05%, the approximate cost drag is 40 × 0.05% = 2%. State first whether the cost is one-way or round-trip and which price is the benchmark, then calculate; simply multiplying by the number of trades can easily give the wrong answer.
2. Think about this: if someone boasts about a strategy with astonishing backtest returns, which three questions should you ask to determine whether they are reporting gross or net return, and how optimistic their execution-price assumptions are? Write the questions down; they will help you avoid many beautiful traps in the future.

---

# Chapter 11: Risk Management—Survive First, Then Think About Winning

From January through June this year, Chen turned $100,000 of capital into $200,000, a full doubling. Over dinner, he animatedly tells you how he did it.

Then July arrives. Chen places a large trade he feels “very sure” about, but gets the direction wrong. Unwilling to accept it, he adds to the position to average down, but the market does not turn around. By the time he finally admits defeat and exits, the $200,000 is down to $40,000.

Now do the brutal math with Chen: to climb from $40,000 back to $200,000, he does not need to earn back the 80% he just lost; he needs a 400% return. The gains from getting every trade right over the first six months were reset, principal and all, in one night in July.

This chapter is not about how to win. It is about something more fundamental: how to reduce the chance that one mistake ends the entire game. No matter how strong your forecasting skill is, it has no time to pay off if your risk limits allow a single tail event to destroy the account.

## 1. Compounding Is Beautiful; Blowing Up Hurts: A Lesson in Asymmetric Arithmetic

Let’s fully unpack Chen’s numbers, because they are the foundation of this chapter.

You have certainly heard of compound interest: “money making money.” You reinvest what you earn to keep earning, like a snowball that grows the longer it rolls. But few people talk about the other side: compounding only works when it has continuity. Hit a large rock along the way, and the snowball shatters; you must rebuild from a small clump of snow. One wipeout voids every gain compounding produced before it.

Gains and losses are mathematically asymmetric. Lose half your money, and earning half back will not make you whole. If $100,000 falls to $50,000, you must double the $50,000 to return to $100,000: a 100% gain, not 50%. Why? Percentages are calculated on the money you have now. Once losses shrink your capital, the same percentage gain produces a smaller dollar amount. The deeper the loss, the more punishing the trap becomes:

<table>
<thead>
<tr>
<th>If you lose</th>
<th>To break even, you must gain</th>
</tr>
</thead>
<tbody>
<tr>
<td>10%</td>
<td>11.1%</td>
</tr>
<tr>
<td>20%</td>
<td>25%</td>
</tr>
<tr>
<td>50%</td>
<td>100%</td>
</tr>
<tr>
<td>80%</td>
<td>400%</td>
</tr>
<tr>
<td>90%</td>
<td>900%</td>
</tr>
</tbody>
</table>

As losses deepen, the return needed to recover rises rapidly according to `loss rate ÷ (1 − loss rate)`. The table does not say losses below 20% are “easy”; it reminds you that the path of loss is asymmetric, and the later you control it, the steeper the required recovery becomes.

Risk management therefore protects against both a single crippling loss and many small, correlated losses accumulating in the same environment. Earning less reduces your ending value; a deep drawdown simultaneously shrinks your capital, makes recovery harder, and may force you to exit at the worst possible time.

## 2. Position Sizing: Do Not Let Any One Bullet Kill You

Since large losses are so deadly, the first line of defense is to limit them at the source. That defense is called **position sizing**.

In plain language, a “position” is how much money you put into a particular trade. Position sizing should answer not “How attractive does this trade look?” but the calmer question: if I am wrong, how badly can this trade hurt me at most?

Position sizing must therefore begin with a risk budget, not with how much you want to make. First decide the maximum damage a trade may cause, then work backward from the exit condition to determine the position size.

Here is an example solely to illustrate the calculation. Suppose an account has $100,000, and you allocate a $1,000 risk budget to a trade in advance. The distance from entry to the price that proves you wrong is 5%. Ignoring fees, gaps, and slippage, the position amount is approximately:

> Risk budget ÷ stop-loss distance = $1,000 ÷ 5% = $20,000

If the price can be exited near the planned level, the book loss is about $1,000. Two qualifications matter here. First, $1,000 is exactly 1% of a $100,000 account; that percentage is only an illustration of a single-trade risk budget, not a universal standard for everyone. The real limit depends on strategy volatility, leverage, liquidity, holding period, portfolio correlation, and the risk you can bear. Second, a stop-loss price does not guarantee execution. Gaps, evaporating liquidity, or system failures can make the actual loss exceed the budget, so position sizing must leave room for such errors.

This method separates “how much you like the trade” from “how much you should bet.” Confidence may affect whether you continue researching, but it must not cross an approved risk boundary: **do not let any single trade have the power to cripple the entire account.**

## 3. Stop-Losses and Circuit Breakers: Two Gates to Automate as Much as Possible

The previous section mentioned exiting when you are wrong. It sounds simple, but it is hard to do because it requires confronting human nature directly. We need two gates written in advance, executed by the system where possible and confirmed through monitoring, rather than leaving the final decision entirely to a panicked version of yourself.

**The first gate: a stop-loss.** This is an exit condition written in advance. It need not be only a fixed price level; it may also be the end of a holding period, excessive volatility, or the disappearance of the condition supporting the original thesis. What they share is that, before entering, you specify what change means the trade is no longer worth keeping.

Writing the stop-loss into the rules in advance prevents moving the goalposts in the moment. But remember one further reality: **a stop-loss can constrain your decision; it cannot guarantee your execution price.** Once triggered, an order may still face gaps, rejection, wider spreads, or insufficient liquidity. A stop-loss must therefore be paired with conservative position sizing and anomaly monitoring; it is not a wall that can never leak.

**The second gate: an intraday loss circuit breaker.** A stop-loss governs one trade; a circuit breaker governs a trading session or the entire account. Once cumulative losses, the number of anomalous orders, or other risk metrics hit a pre-approved boundary, the system stops taking on new risk, cancels cancellable open orders, and alerts the responsible person to review.

Our lab once set a **5%** daily loss limit for a certain class of accounts. That number was an internal choice for a particular capital base, strategy, and risk tolerance. The non-negotiable point is not “it must be 5%,” but that the boundary must be set while calm and must not be loosened in production because “this time is different.”[^risk-five-percent]

[^risk-five-percent]: This was an internal choice for a specific account, not a universal safety parameter or risk advice readers can copy; boundaries should be set individually based on capital, strategy volatility, liquidity, and tolerable loss.

> **⚠️ Common Misconceptions**
>
>
> **Misconception 1: “Using a stop-loss means admitting you are bad. Experts hold on.”** A stop-loss does not admit “I am bad”; it admits “I cannot be right every time.” The genuinely professional approach is to define when a judgment has failed, then limit the loss on one trade to what the portfolio can bear.
>
>
> **Misconception 2: “It is enough to keep the stop-loss in my head; I can cut it manually later.”** Exit conditions kept only in your head are easiest to reinterpret while losing. It becomes a complete gate only when written into the rules, triggered automatically where possible, and checked to ensure the order was actually sent and filled.

## 4. Never Hold On and Add Ad Hoc: A Loss Cannot Rewrite Your Risk Budget

Here, “holding on” does not mean every instance of continuing to buy after a price falls. Scaling into a position that is written into the strategy in advance and does not increase total risk, or rebalancing under fixed rules, can be normal design. The truly dangerous action is different: a position is already losing, the original rules do not call for adding, yet you temporarily enlarge it to lower the average cost while pushing the original exit condition farther away.

This kind of ad hoc adding can sound reasonable. “The price is cheaper now.” “A small bounce will get me out.” Every line sounds like analysis, but often it is merely an excuse for refusing to admit you were wrong. It does two harmful things at once: it increases risk as the evidence worsens and makes the prewritten stop-loss ineffective.

It is especially deceptive because many small drawdowns really do rebound. You may escape several times in a row by holding on and adding, and learn a dangerous lesson: as long as you never admit defeat, the market will eventually come back. But when a sustained trend, a gap, or evaporating liquidity arrives, the accumulated oversized position can let one loss swallow many prior small wins.

So what the lab truly prohibits is **unregistered risk that is increased ad hoc because of a loss**. If you want to scale in, state before entry the conditions for every tranche, the maximum total position, and the final exit line. Do not wait until a loss occurs and then dress up an impulse as a strategy.

## 5. Martingale: Hiding a Rare Catastrophic Loss Behind a String of Small Wins

Holding on and adding has a more extreme, systematic cousin: the **Martingale**. It is often packaged as a high-win-rate robot: every time it loses, it doubles the next bet; as long as a later bet wins, it covers the preceding losses and earns the original small gain on top.

The numbers do grow that way: 1, 2, 4, 8, 16... After ten consecutive losses, you have already lost 1,023, and must bet 1,024 next merely to net the original 1. In any one round, ten straight losses may be uncommon; but if you run many rounds repeatedly, you will get ever closer to the losing streak that your capital, margin, or exchange limits can no longer absorb.

More importantly, doubling down **does not turn a negative-expectancy game into a positive-expectancy one**. In an environment with fees, spreads, or a house edge, the disadvantage of every bet remains. Martingale merely reshapes the profit-and-loss profile: it exchanges many small wins for a few very large losses. It makes the curve look smooth and the win rate look astonishing for a long time, while pushing the real risk into the tail, waiting to settle it all on one ordinary bad day.

**With finite capital, finite credit, and finite execution capacity, persistent use of Martingale accumulates an unacceptable risk of ruin; trading costs make it worse.** That alone is enough to exclude it from a responsible risk-management system.

> **🔬 A Lesson from Practice: Three Rules That Cannot Be Relaxed on the Fly**
>
>
> The lab puts three rules into its systems and governance process:
>
>
> 1. When the approved intraday loss limit mentioned earlier is reached, trigger the circuit breaker and stop.
> 2. No loss-driven adding unless it was registered in advance.
> 3. No Martingale-style increases in position size.
>
>
> The reason is simple: after a loss, people easily interpret “special circumstances may justify an exception” as permission to relax a boundary temporarily. A crack for one exception soon becomes an open door.
>
>
> When the market is volatile and losses are nearing the circuit-breaker line, “this time is different” sounds especially persuasive. A rule is a real boundary only if it still operates in that moment.
>
>
> Machines execute approved boundaries; people approve deployment, capital transfers, risk limits, and scaling. Chapter 13 explains this division of responsibility.
>
>
> These controls add operational friction, but that friction is meant to stop a one-time exception during a loss. Discipline is most valuable precisely when people are most anxious and most tempted to rewrite the rules.

## 6. Think Differently: Treat Risk as a Budget You Spend First

The first five sections covered tools such as position sizing, stops, circuit breakers, and prohibitions on adding to losses. One more fundamental sequence must now be reversed: risk should be an ex ante budget, not an after-the-fact addition.

Most beginners think like this: first find a great opportunity and consider how much it could make them; then—if they remember—add, “Oh right, set a stop-loss.” In that sequence, risk is an afterthought. The professional approach reverses the order: **allocate risk first, then look for opportunities.**

Think of it this way. You receive a fixed salary each month. Someone who understands personal finance sets a budget first—how much for rent, food, and entertainment—then lives within it. They do not shop wildly and panic at month-end, asking, “How much did I spend?” Risk is that budget in the trading world. Based on what the strategy and account can bear, you first decide how much risk may be used per trade, per day, and at the portfolio level. Those boundaries are approved before emotion appears and before a single dollar is put at risk; every subsequent trade must remain within them.

The difference between the two sequences appears under pressure. If risk is added afterward, an attractive opportunity can easily persuade people to relax it. A risk budget allocated in advance is an explicit boundary that no opportunity, however tempting, may cross.

This is where the subtitle of this book becomes most concrete. **The pessimist’s tools** ask first: “How could this lose?” “Could the actual fill be worse?” “What happens if several defenses fail at once?” Then they design position sizes and limits for the bad case. **The optimist’s heart** is not the belief that every trade will win. It is the belief that, as long as one mistake has not thrown you out of the game, you will have another chance to learn, adjust, and wait for your edge to pay off.

Risk management does not make a bad strategy good. It does something more fundamental: it tries not to let any single judgment easily end the entire game for you.

> **📌 Chapter Takeaways**
>
>
> - **One large loss breaks the continuity of compounding.** A 50% loss needs a 100% gain to recover; a 90% loss needs 900%. Limiting major losses matters more than chasing a single windfall.
> - **Position size is derived from the risk budget.** First decide how deeply the trade may hurt, then calculate the position from exit distance, liquidity, leverage, and gap risk. The percentages in this book are examples, not universal prescriptions.
> - **Stop-losses constrain decisions; they do not guarantee prices.** Exit conditions and intraday circuit breakers should be approved in advance, automated where possible, and monitored; actual fills may still be worse than planned.
> - **What is prohibited is ad hoc holding on and adding.** Preplanned scaling into a position without increasing total risk differs from expanding a position on your own after a loss to average down.
> - **Martingale hides tail risk behind a high win rate.** Doubling does not turn negative expectancy positive; finite capital and trading limits eventually make long losing streaks unbearable.
> - **Allocate risk first, then seek opportunities.** Risk management cannot rescue a bad strategy, but it can reduce the chance that one mistake ends the entire game.
>
>
> **✍️ Try It / Think About It**
>
>
> 1. **Calculate your “cost of recovery.”** Suppose you have $100,000 of capital. Calculate what percentage you must earn on the remaining money to return to $100,000 after losing 30%, 60%, and 85%, respectively. Write down the three numbers and stare at them for 30 seconds. Feeling this asymmetry will protect you better than any lecture.
> 2. **Write a risk budget for a hypothetical strategy.** Write down four items: (a) the maximum risk per trade; (b) portfolio-level and daily limits; (c) room for slippage or gaps after a stop-loss triggers; and (d) whether scaling into a position is allowed and, if so, when the total position is capped. The numbers must come from strategy volatility and losses you can bear, not from copying the examples in this book.

---

# Chapter 12: Portfolios—Don't Put All Your Eggs in One Correlation Basket

## 1. “I Bought Ten Coins, So I’m Diversified, Right?”

Lin divided his capital into ten parts and bought ten different cryptocurrencies, assuming that if one failed, the other nine would support him. Then the market fell over a weekend and all ten dropped at nearly the same time by similar amounts. He had not bought ten independent eggs; it was more like photographing the same egg ten times and putting one photograph in each of ten baskets.

The problem was not too few holding names, but that the assets were exposed to similar risks. Diversification is not only about counting positions; it also depends on the **correlation** among them.

## 2. What Diversification Really Means: Correlation, Not Quantity

First, let’s explain a term we will use repeatedly in this chapter: **correlation**.

Correlation describes **the degree to which two sets of returns move linearly in the same or opposite direction over a sample period**. Put simply: how often do two things move together? It measures co-movement, not merely how many days they move in the same direction; and its value changes with the frequency, window, and market regime.

- When B almost always rises when A rises, and falls when A falls, they have **high positive correlation**. They are like two people walking tied together: when you walk, I walk.
- When B often falls when A rises, they have **negative correlation**. They are like a seesaw: one side goes up while the other goes down.
- When A’s linear changes are hard to explain with B’s changes, their **correlation is close to 0**. That does not mean they have no relationship at all, nor that they cannot fall together in extreme conditions.

Quantitative traders commonly use a number from **-1 to +1**, called the correlation coefficient, to describe this. You do not need to know how to calculate it; just remember three anchors:

> **+1** = perfectly synchronized, hand in hand (moving together identically)
> **0** = no obvious linear synchronization (but not complete independence)
> **-1** = perfectly opposite movement (when one rises, the other must fall)

**The power of diversification comes not from how many things you buy, but from how little they move together.**

Let’s use Lin’s example to make this clear. Suppose each asset has some standalone volatility risk—the amount it can swing around on its own.

- **Case A (Lin’s case):** ten coins with correlations close to +1. They move almost in sync. Put all ten together and the portfolio’s overall swings **will barely become smaller**. Because they swing in the same direction at the same time, their force adds up rather than offsets. You think you are diversified, but portfolio risk is not much different from owning one coin.
- **Case B (more effective diversification):** ten holdings with lower correlations, and with weights that do not let one holding dominate the risk. In this case, some gains and losses offset each other, and portfolio volatility will usually be lower than concentrating capital in one representative high-risk holding.

Diversification is therefore often called the closest thing to a “free lunch”: **it does not guarantee unchanged returns, but it can reduce a portfolio’s dependence on a single source of risk.** Its true benefit is not earning more out of thin air, but making one surprise less likely to determine the entire outcome.

So when someone says, “I own twenty names,” first ask whether those twenty are exposed to the same risks and whether they tend to fall together under stress. The number of names does not by itself prove diversification.

## 3. Why Does Diversification Weaken in a Crisis?

Is low correlation in ordinary periods enough to make a portfolio safe? No. **Correlation is not a fixed constant.** It changes with market regime, estimation window, and participant behavior. Assets that move separately in calm periods may all be sold when liquidity tightens or the whole market deleverages, causing their correlations to rise sharply; some pairs may even move almost in lockstep for a time.

Why? In a crisis, many people are not selling one particular story; they are selling “risk” on their balance sheets. They need cash for margin, funds need to liquidate to meet redemptions, and traders simply want to get back to cash first. The same funding pressure then pushes different assets in the same direction.

To be precise, not every correlation automatically becomes +1 in every crisis, and not all diversification fails completely. A more reliable conclusion is: **protection based on historically low correlation often shrinks during stress.** If your portfolio appears diversified only in calm samples, that sense of safety is too thin.

So portfolio construction cannot rely on one full-period average correlation coefficient. You must also examine rolling correlations, stress periods, shared sources of liquidity, and whether several assets are actually bets on the same hidden risk. Diversification reduces everyday concentration; the position sizing and loss limits from the previous chapter control the damage when diversification weakens. They complement each other; neither can replace the other.

## 4. How Can Multiple Strategies and Holdings Complement One Another?

Instruments can diversify one another, and so can strategies sharing the same capital. The deeper question is whether those strategies rely on different mechanisms and whether their losing periods genuinely occur at different times.

First, a quick explanation. In earlier chapters, we described a “strategy” as a fixed trading rule: under what conditions to buy and under what conditions to sell. Different strategies earn **different kinds of money** from markets:

- Some strategies earn from **trend following**: they enter as prices rise, betting the rise will continue.
- Some strategies earn from **mean reversion**: they buy after a sharp decline, betting the price will bounce back.
- Some strategies earn from **spreads**: they repeatedly capture small price differences between two places.

**Strategies based on different mechanisms may perform differently across market regimes.**

A trend-following strategy may benefit from a clear trend yet suffer repeated small losses in a choppy market. A mean-reversion strategy may do better in a range but suffer during a persistent one-way move.

The losing periods of the two strategies may occur at different times, but this cannot be judged from a story alone. It must be tested using return series from the same period and under the same cost assumptions. Only when the low-correlation relationship survives testing can the combination reduce the volatility contributed by either strategy alone.[^low-correlation]

[^low-correlation]: Low correlation cannot make negative expectancy acceptable; you must still examine net returns after costs, tail risk, liquidity, and correlation during stress periods.

When several strategies are in use, examine both their individual net returns and the combined portfolio. A strategy that is unremarkable on its own may still add portfolio value if it supports the others during their weak periods. If every strategy always gains and loses at the same time, additional names add little diversification.

Evaluating a new strategy therefore requires more than asking whether it has a positive net expectation on its own. Ask what it does after joining the existing portfolio: does it reduce total risk, or merely add another copy of the same exposure?

A strategy with positive net expectancy, or a clear hedging purpose, may not look impressive on its own. But if it fills in during other members’ slumps, its contribution to the portfolio may exceed that of a star strategy that only adds more of the same at the same time.

## 5. How Should You Allocate the Money? From Equal Weighting to Risk Parity

All right. Suppose you have chosen several members that are not highly correlated, whether assets or strategies. The next practical question is:

**How should I divide my money among them?**

Let’s start with the most intuitive and honest approach.

### Method 1: Equal Weighting (An Even Split)

The simplest approach is to give **every member the same amount of money**. With five members, each receives 20%. This is called **equal weighting**.

The advantage of equal weighting is that **it does not require a forecast of which member will perform best**. As a research benchmark, it also gives more complex allocation methods a plain comparison they must beat. It is not an investment prescription for every account; when members differ greatly in volatility and liquidity, equal weights may still concentrate risk heavily.

### The Blind Spot of Equal Weighting: Equal Money Does Not Mean Equal Risk

Suppose you have two members and split the money evenly, 50% each:

- Member A is a calm asset that moves at most 1% a day.
- Member B is a wild asset that can move 10% a day.

The money is indeed split evenly—half for each. But what about **risk**? The daily heartbeat of your portfolio is governed almost entirely by B. It moves 10% while A moves only 1%; B’s swings completely drown out A’s. You think you have split the portfolio fifty-fifty, but most of its volatility risk actually comes from the wild B.

Equal capital weights do not imply equal risk contributions.

That leads to the second approach.

### Method 2: Risk Parity (Balancing Risk Contributions)

The core idea of **risk parity** is:

> **Do not merely give every member the same amount of money. Try instead to make their contributions to portfolio risk more balanced.**

How? Intuitively: **put less money into members that swing wildly, and more into members that move gently.** After that adjustment, the volatility each member creates for the portfolio can become more similar, reducing the chance that one member alone hijacks the entire equity curve.

Return to the example: wild B moves 10% a day, while calm A moves 1%. If we temporarily ignore their correlation, the inverse-volatility intuition says B should receive roughly one-tenth as much capital as A for their volatility contributions to be similar. **This is only a beginner’s intuition, not complete risk parity.** A formal calculation puts correlation into the covariance matrix and estimates each member’s marginal contribution to portfolio volatility. Allocating more capital to low-volatility assets may also require leverage to reach a target return or volatility, bringing financing, margin, and tail risk into the equation.

The difference between the two can be summarized as follows:

- **Equal weighting:** everyone gets an equally large seat. Simple, honest, and less prone to false cleverness.
- **Risk parity:** try to make everyone’s risk contribution to “whether the boat capsizes” more balanced. It is closer to the nature of risk, but requires estimating volatility and correlation.

A practical research sequence is: **use equal weighting as the benchmark first, then test more complex allocations.** If you adopt risk parity, you must also check whether covariance estimates are stable, whether rebalancing costs consume the benefit, and whether leverage on low-volatility assets introduces new tail risk. Any complex allocation method should prove more useful than a simple benchmark out of sample and after costs.

## 6. Portfolio-Level Risk: Looking at One Piece Is Never Enough

The preceding sections considered how members are selected and allocated, but portfolio risk cannot be inferred by inspecting each part separately. Every strategy and instrument may look sound on its own while the combination remains exposed to the same underlying risk.

Risk must therefore be measured at the **portfolio level**.

Ten strategies with attractive standalone backtests may still suffer together if they gain and lose in the same market regime. What appears to be ten strategies may be ten expressions of the same risk exposure. That is why the next step must examine the combined equity curve.

So you cannot judge the health of a portfolio by reading ten attractive individual report cards. You must **stack them together** and look at the **combined overall curve**:

- How violently does it swing overall?
- How deeply has it fallen at most from a historical high in this sample? (This is called **maximum drawdown**. It is a path-dependent historical statistic, not the worst future loss, but it often comes closer to the real stress of holding a portfolio than average return does.)
- Are all of these members betting on the same kind of “market weather”?

A portfolio audit cannot be satisfied with “every component looks fine on its own.” It must also stress-test common shocks, evaporating liquidity, and rising correlations, asking: **when several seemingly independent risks occur at once, could the loss exceed the account’s boundaries?**

Diversification does not promise riches, nor does it block every systemic shock. What it does is reduce dependence on a single member and a single mechanism, making one local surprise less likely to determine the whole outcome.

And “staying alive long enough” is the starting point of the previous chapter on risk management. In the next chapter, we will take these boundaries into a real production-launch process.

> ### ⚠️ Common Misconceptions
>
>
> **Misconception 1: “If I own enough, I am diversified.”** Diversification depends on shared risk, not the number of names. Ten assets that often rise and fall together may still concentrate exposure to the same risk.
>
>
> **Misconception 2: “Correlation was low over the full period, so it will protect me in a crisis.”** Not necessarily. Correlation changes with market conditions and can rise during stress because of common deleveraging. In addition to averages, examine rolling windows and stress samples, and use the portfolio risk boundaries from Chapter 11 to withstand a breakdown in correlation.

## 📌 Chapter Takeaways

- **Diversification is about shared risk, not just the number of names.** A correlation coefficient of 0 only means no obvious linear synchronization; it does not mean complete independence.
- **Diversification is the closest thing to a “free lunch,” but it does not guarantee returns.** Its value is reducing a portfolio’s dependence on a single source of risk, not increasing returns out of thin air.
- **Correlation changes with conditions.** Common deleveraging during stress often weakens protection from low correlations; examine rolling correlations and stress samples, not only full-period averages.
- **With multiple strategies, examine the combined curve.** A member that looks unremarkable alone but fills in during another strategy’s slump may be more valuable than a star strategy that rises in sync with the others.
- **Equal weighting is an honest benchmark; risk parity focuses on risk contribution.** Inverse volatility is only the intuitive version; complete risk contribution also depends on the covariance among members.
- **Risk lives at the portfolio level.** Only by viewing all positions together—the volatility, maximum drawdown, and hidden common exposures—can you know how many times you are really making the same bet.

## ✍️ Try It / Think About It

1. **List a basket you own or plan to study**, choosing five to ten instruments. Using returns at the same frequency, calculate correlations for normal periods and for at least one stress window, then examine the largest common decline and shared sources of liquidity. Do not rely on memory to ask, “Did they fall together last time?” Put normal and stress samples side by side to see whether diversification protection has weakened.
2. **Run a small thought experiment:** suppose two members have daily volatilities of about 2% and 8%. First ignore correlation and use the inverse-volatility intuition to estimate how to allocate them so their volatility contributions are similar. Then ask one more question: if they always surge and plunge in the same direction on the same days, why is this rough calculation still insufficient?

---

# Chapter 13: From Research to Live Trading: Governance, Discipline, and the Irreversible Gate

A strategy has completed data cleaning, signal design, cost estimation, and out-of-sample testing. The cursor rests over a button that looks almost identical to “Run Backtest,” except that this one says “Start Live Trading.”

The appearance is similar; the consequences are not. A backtest can be rerun. Once a live order reaches the exchange, its execution price and any resulting loss cannot be undone. There is no Ctrl+Z.

An **irreversible gate** therefore separates paper research from real money. Passing the preceding statistical and risk checks means only that the strategy is eligible to approach the gate, not that it may cross with a large amount of capital at once.

This chapter explains how to cross the gate in stages, what evidence each stage requires, and who should approve the risk boundaries.

## 1. Passing on Paper Does Not Mean It Can Run in Reality

Chapter 7 explained that backtesting can eliminate ideas that clearly do not hold up, but it cannot guarantee real-world execution. At this point, we will not repeat what a backtest is. We will focus on the gap between it and live trading—the gap people most often overlook.

In a paper model, market data is tidy. In a real market, orders wait in queues, networks lag, exchanges reject orders, and liquidity can suddenly thin out exactly when you need it most. Your program may also contain a bug that appears only in real-time operation. More importantly, once positions get larger, your own orders start changing the prices at which you trade.

So passing on paper earns only the right to enter controlled validation. Your execution assumptions, system stability, and capacity at scale must each be measured under strict limits. The purpose is not to prove as quickly as possible that the strategy makes money. It is to learn, at the lowest possible cost, how far the paper world is from reality.

This brings us to the backbone of the chapter: staged rollout.

## 2. Staged Rollout: Enter the Water One Step at a Time

A strategy should enter live trading the way a swimmer moves from shallow water to deep water: in stages, with each stage testing only a limited set of questions and limiting the possible loss.

**Stage one: paper trading.** Connect real-time or near-real-time data using pretend money, and first validate the wiring and state machine. Do order placement, modification, and cancellation work correctly? Do timestamps and positions reconcile? Does the program crash when prices jump sharply? But simulated fills are often unrealistic—they may ignore queue position, partial fills, and the process of consuming the order book yourself. So this stage shows only that “the engineering workflow basically runs,” not that “live orders will fill at the same prices.”

**Stage two: live trading at the minimum executable size.** Only once paper trading runs smoothly should you use real money—and then only at the smallest reasonable size the exchange allows that is still large enough to experience real execution friction. The amount should be small enough that a failed validation will not seriously hurt you. Here, for the first time, you measure real queues, partial fills, slippage, fees, and rejected orders. Every live fill should be compared with the backtest assumptions, and you must not look only at averages: the worst tail observations, the unfilled-order rate, and abnormal retries often reveal more than the mean.

**Stage three: gradual scaling.** Increase size only after small-scale live trading holds up. Net returns at small scale cannot be extrapolated linearly to large scale; as orders grow, market impact and non-fill rates may rise. At every increase, re-estimate costs, capacity, and risk. If a metric deteriorates to a predefined boundary, return to the previous stage.

All three stages need graduation criteria written in advance. Paper trading checks the engineering process; small-scale live trading measures real-world deviations; scaling re-estimates whether size is eroding the edge. If the standard is not met, remain at the current stage. Connecting these “the gate stays closed unless the standard is met” checkpoints creates the governance chain in the next section.

## 3. The Governance Chain: A Series of Gates That Do Not Let You Through Easily

Link those checkpoints together, and you have a **governance chain (governance)**.

A **governance chain** defines who may approve what, what evidence the approval requires, and what conditions force a stop. A strategy can enter the next stage only after its backtest, risk parameters, and monitoring pass their respective **gates**. Without any one required sign-off, the gate remains closed.

One crucial default is **fail-closed**—plainly, “when something goes wrong, shut it down.” It applies mainly to **risk-critical states**: when data is stale, positions do not reconcile, permissions are unclear, or a key check fails, the system should by default stop adding risk and refuse to scale up or switch to live trading, rather than “run first and sort it out later.” Non-critical alerts may be handled at a lower severity, but what counts as critical must be written down in advance.

The default must be conservative because, when a risk-critical state cannot be explained clearly, continuing to run can turn a small, diagnosable problem into a real-money loss. New risk is permitted only when both the evidence and the responsible owner are clear. If the state of the data, positions, or permissions is ambiguous, authorization stops.

These controls reduce speed, but they leave a record of every opening of a gate and every temporary relaxation. Their purpose is not to eliminate every failure, but to prevent a system from expanding risk on its own when nobody is accountable and the evidence is insufficient.

## 4. The Irreversible Boundary: People Approve the Boundary; Machines Execute Within It

“Human-in-the-loop” is often misunderstood to mean a person must manually click every live order. That would turn systematic trading back into manual trading, and it does not suit strategies that need timely execution.

A more sensible division of labor is: **people approve risk boundaries; machines execute within those boundaries.** Switching to live trading, placing the first real order, adding capital, raising leverage or position limits, expanding the instruments traded, changing the core strategy, or granting new API permissions—actions that change the maximum possible loss or the system’s behavior—must be reviewed by a person and leave an accountability record. Once approved, routine orders may run automatically within the predefined instruments, size, frequency, and loss boundaries.

Why deliberately keep friction around boundary-changing actions? Because they change how deeply the system can hurt you. A machine can execute approved rules at high speed, but it cannot decide on behalf of the account owner how much risk to bear. Putting human checks at the boundary preserves the discipline of automation while preventing a program from expanding its authority unnoticed.

A mature governance chain should therefore answer three questions: who is authorized to open which gate? What evidence did they review when approving it? If something goes wrong, can the decision be traced back to that approval? Without these records, “someone is accountable” is only a slogan.

## 5. Do Not Leave the Keys Lying Around: Credentials and Security

To let a program trade automatically for you, you must give it a key so it can log in to the exchange and place orders on your behalf. This key is an **API key**—think of it as your home’s access card. Whoever has it can use your account.

Credential management must observe at least three rules:

- **Never paste a key into a chat window or hard-code it in source code.** Never upload it to a public repository. Put it in a dedicated secrets-management tool or protected environment variables, limit who can read it, and keep a way to rotate and revoke it. Exposed credentials can be quickly exploited by automated scanners; do not assume that deleting them means nobody saw them.
- **Keep live-trading and paper-trading keys separate.** Stage-one paper trading (demo) uses a toy key; stage-two-and-beyond live trading (live) uses a real key. Never put these two keys in the same drawer or give them the same name. One day you will be rushing, and rushing is when you are most likely to grab the wrong key—you think you are testing in paper trading, but you are actually placing orders with real money. Keeping live and demo fully separate from the credential level onward safeguards a future, panicked version of you.
- **Give the program as little permission as possible.** Enable only the trading permissions the strategy genuinely needs, and disable withdrawals. Where the platform supports them, also add IP allowlists, subaccounts, and spending limits. Disabling withdrawals reduces one form of harm, but it does not make a leaked credential safe—an attacker may still cause severe losses through malicious trades.

These measures cannot eliminate the risk of credential exposure, but they can limit the damage caused by one credential error.

## 6. Install the Dashboard and Red Button Before Going Live

Monitoring and a kill switch must be in place before real money begins to run.

The first is **monitoring**: your dashboard and alerting system. At a pace appropriate to the strategy’s risk clock, it should at least show your current positions, realized and unrealized P&L, open and rejected orders, whether data is fresh, and how close you are to risk limits. A low-frequency strategy may not need someone watching the screen all day, but every anomaly must be detected and escalated to an owner while there is still time to act.

Chapter 5 discussed silent failure. Live monitoring likewise cannot check only whether the program is alive. Internal positions, orders, and fills must be reconciled regularly against broker or exchange records. Order retries should use a unique order identifier so that network instability does not turn one intended order into two real ones.

The second is a **circuit breaker**: your emergency brake, or kill switch. When triggered, it first stops adding risk, cancels unfilled orders, then attempts to reduce or close positions according to the plan and notifies the owner. We must be honest here: **a kill switch does not guarantee that every position can be closed instantly in every market.** If the exchange is down, the order book is empty, or prices gap, the commands may also fail. So both automatic circuit breakers and manual switches must be rehearsed regularly, while position limits remain the earlier, first line of defense.

These two things must be installed before real money. If you start looking for logs or writing a liquidation script only after trouble begins, it is usually already too late. Monitoring finds trouble early; the kill switch stops the risk from continuing to grow. Neither can replace limits set in advance.

> **⚠️ Common Misconceptions**
>
>
> **Misconception 1: “The backtest made a killing, so I will go straight to big money. Going slowly wastes opportunities.”** This is expensive impatience. Skipping paper trading and small-scale live trading means using your capital to pay for the gap between paper and reality before you have even measured it. A staged rollout is not cowardice; it breaks unknown risks into smaller pieces.
>
>
> **Misconception 2: “It is automated, so once it is set up, I can leave it alone, right?”** Automated trading can run without a person clicking every order, but it cannot run without someone being responsible. The system needs alerts, an on-call arrangement, an escalation path, and a clear owner. Automation reduces manual actions; it does not remove accountability.
>
>
> **🔬 A Lesson from Practice: The Machine That Stopped at 3 A.M.**
>
>
> The lab's automated programs can find hypotheses, run backtests, write code, and archive results.
>
>
> But for any action that changes a real-money risk boundary, the program may prepare the materials but may not approve the action itself.
>
>
> One night, a strategy passed the preceding gates and was ready to send its first real order. The system displayed the order size, expected execution, loss scenarios, and risk limits, then waited for human confirmation. At 3 A.M., the on-call person reviewed the figures before approving deployment.
>
>
> The design is inconvenient. But this was the strategy's **first order** crossing from paper into live trading, and the first opening of its risk boundary. The person was not approving every future routine order; they were approving the scope within which the automated execution system could operate. Once the scope was approved, the machine executed inside it. Expanding the scope required passing through the gate again.
>
>
> The rule adds waiting time, but it preserves a clear record of responsibility when the risk boundary is opened for the first time.
>
>
> **📌 Chapter Takeaways**
>
>
> - **Passing on paper earns only the right to controlled validation.** Paper trading tests the engineering; minimum-size live trading tests execution; gradual scaling tests capacity.
> - **Every stage needs predefined graduation criteria.** If they are not met, stay where you are; “let us run it a little bigger and see” is not validation.
> - **The governance chain defaults to fail-closed.** When data are stale, a check fails, or the state is unclear, stop adding risk by default rather than run first and explain later.
> - **People approve boundaries; machines execute within them.** Going live, moving capital, permissions, risk limits, and scaling require human approval; routine orders may run automatically under approved rules.
> - **Credentials use least privilege and layered isolation.** Disabling withdrawals and using subaccounts or allowlists can reduce harm, but cannot eliminate the risk of exposure.
> - **Monitoring and a kill switch must come before real money.** A kill switch can stop new orders, cancel orders, and attempt to reduce positions, but cannot guarantee instant liquidation in every market condition; pre-set position limits remain indispensable.
>
>
> **✍️ Try It / Think About It**
>
>
> 1. Take out paper and pen and write graduation criteria for a hypothetical strategy's three stages. Which engineering tests must paper trading pass? At minimum-size live trading, how many valid fills must you accumulate, and what predefined ranges must median slippage, tail slippage, and rejection rate fall within? After scaling, which worsening metrics would send you back to the previous stage? Do not write, “It feels good enough.”
> 2. Consider a tool that tells you, “I will trade fully automatically for you—link your account, start with one click, and never worry about it.” After reading this chapter, what three questions would you ask? (Hint: What permissions does the key have? Where is the kill switch, and how do you activate it? Who is responsible when something goes wrong?)

---

# Chapter 14: Common Traps and Human Nature: Confirmation Bias, Revenge Trading, and Sunk Costs

## You Can Fix Programs—but Can You Fix Yourself?

The preceding chapters dealt with backtesting, statistics, and transaction costs. Technical errors can be found through tests, logs, or reconciliation; a person's interpretation of evidence can shift with emotion.

Psychological biases do not necessarily make the system throw an error. Instead, they generate a pleasant explanation for the decision: calling a strategy that should be cut “only temporarily broken,” calling luck skill, and calling the moment to stop a rare opportunity.

This chapter examines how these biases enter research and trading decisions, and how process can constrain them.

We will take them apart one by one: why you fall in love with your strategy (confirmation bias), why you want to win it back immediately after a loss (revenge trading), why you cannot bear to cut a bad strategy (the sunk-cost fallacy), and why a losing streak makes you think the next trade “should” win while one lucky outcome gets dressed up as skill (the gambler’s fallacy and self-serving attribution bias). Finally, we will turn these vulnerabilities into paths that systems and peers can block.

## Confirmation Bias: We Are Born Biased Toward Our Own Children

**Confirmation bias** is the tendency to seek evidence that supports your own idea while applying a harsher standard to evidence against it.

Here is an everyday example. You decide that a certain brand is especially reliable. Afterward, you actively save positive reviews about it; when you encounter a negative review, you quickly explain it away as “that person does not know how to use it” or “it is just one unusual case.” The evidence is not being measured by the same ruler—supporting evidence is kept, while opposing evidence is relabeled.

After spending three weekends producing an attractive curve, you can easily begin defending it instead of continuing to test it:

- You will screenshot and revisit the months when it performs well, thinking, “See? I told you so.”
- You will find excuses for the months when it performs badly: “The market was too abnormal then,” or “That was a black swan; it does not count.”
- When someone points out its problems, you rush to defend it instead of rushing to verify them.

At that point, the researcher has shifted from testing the strategy to arguing for it. A scientist asks what is true; a lawyer seeks the interpretation most favorable to a client. Once the roles are quietly exchanged, the same evidence is measured by two different standards.

The lab limits this bias with an ex ante contract: **write down what result would prove you wrong before looking at the data.**

The falsification contract in Chapter 6 and the preregistration in Chapter 8 already provide technical defenses. Here we are looking at the psychological layer: once you fall in love with your strategy, you will instinctively find excuses for exceptions and reinterpret the threshold for failure. A written contract cannot eliminate bias, but it can leave a trace of it. Add a review by someone who did not participate in building the model, and you are less likely to be trader, referee, and defense lawyer all at once.

> **⚠️ Common Misconception**
> “I have a lot of confidence in this strategy.” — Confidence may make you willing to keep investigating, but it cannot add weight to the evidence. The less you can bear for it to fail, the more you need to write down counterexamples, reasons for changes, and opposing views in advance. The healthy statement is not “I believe it will work,” but “I have listed the conditions that would make it lose support; here is what the evidence shows so far.”

## Revenge Trading: The Urge to “Win It Back Right Away”

Another common problem is **revenge trading**.

You lose money on a trade in the morning, and the loss sticks in your mind like a thorn. A voice says, “No, I have to make it back right now.” So you increase the next position size or take a trade your rules never called for. The goal is no longer to execute an edge, but to restore the account balance to a number that makes you feel comfortable.

The market does not know that you lost money this morning, and it owes you nothing. The last loss and the next opportunity must be connected by a new mechanism and new evidence; “I cannot accept it” is not a mechanism. Revenge trading expands freedom to place orders precisely when judgment is hardest to maintain.

Chapter 11 covered intraday loss limits, and Chapter 13 covered how to have systems enforce them. Here is the psychological reason to add: after a limit is triggered, people instinctively interpret stopping as “admitting defeat” and continuing to trade as “a chance to come back.” A truly effective kill switch must therefore do more than stop new orders; it must create enough friction—revoking permissions, locking the interface, notifying a peer—that an overheated version of you cannot disable the rule with a single click.

## Sunk Costs: What You Cannot Let Go Of Is Really Those Three Weekends

The third trap is related to confirmation bias but more subtle: the **sunk-cost fallacy**.

Sunk costs are time, money, and effort already spent and impossible to recover. The sunk-cost fallacy is continuing to commit more resources to a low-value choice because you cannot bear to let those earlier investments go.

The classic everyday example: you buy a movie ticket, then discover ten minutes in that the film is terrible. The rational choice is to leave and use the remaining hour and a half on something else. But many people think, “I already paid for the ticket; what a waste,” and force themselves to stay seated through two miserable hours. The ticket money cannot be recovered whether you stay or leave—it has “sunk.” Yet because of it, you also waste another hour and a half.

In research, this trap looks like this: you spend three entire weekends tuning a strategy, making dozens of versions, and it is just not very good. The rational move is to admit, “This path does not work; cut it.” But you think, “I put three weekends into this. If I quit now, were those three weekends not wasted?” So you spend a fourth and fifth weekend trying to rescue something that should have been let go.

Those three weekends are already spent; continuing or ending the project cannot bring them back. What remains in your hands is the fourth weekend. Separating those two accounts lets you move from “I cannot abandon the past” to “Is the next step worth taking?”

The lab therefore writes the principle in one sentence: **rejecting an idea is not failure.**

Beginners often feel that cutting a strategy and admitting it does not work means all three weekends were wasted. A more accurate approach separates past investment from future decisions: whether those three weekends become knowledge depends on whether you leave behind conclusions others can review; whether to spend the fourth weekend depends only on the expected information value of the next step, not on how much you have already spent.

> **⚠️ Common Misconception**
> “I’ve come this far; if I just hold on a little longer, it might work.” — Separate two things clearly: whether a project should continue depends only on its expected value from now onward—how much information the next step can add, what it costs, and what alternative projects exist—not on the amount already invested. Every time you want to use “I’ve already spent so much” as a reason to continue, an alarm should go off.

## The Gambler’s Fallacy and Self-Serving Attribution: Do Not Dress Luck in the Clothes of Skill

Now for two related traps, both about how poorly we distinguish luck from skill.

The first is the **gambler’s fallacy**.

The gambler's fallacy is believing, without evidence of a mechanism, that a run of outcomes “must be made up for”: after five reds in a row, the next spin ought to be black.

In a roulette wheel where each round is independent and probabilities do not change, the first five spins do not change the sixth. Markets, of course, may not be independently and identically distributed; trends and regime changes can exist. But **a losing streak by itself does not prove that the next trade has a higher chance of winning**. To increase position size, you need a new mechanism and new data—not “it has to be my turn by now.”

The second is subtler: **self-serving attribution bias**—using two different explanations for good and bad outcomes. When we profit, it is because we are skilled; when we lose, it is because of bad luck or an abnormal market.

This double standard makes people systematically overestimate themselves. One lucky bet on a sharp rise may be interpreted as “insight” and “courage,” then repeated with a larger position. Without a consistent standard for attribution, a single stroke of luck can teach the wrong lesson.

To handle this, do not investigate only after losses and pop champagne after profits. Both wins and losses must go through the same attribution audit: write expectations in advance, then break down market exposure, costs, execution deviations, exceptional events, and sampling uncertainty afterward. Also ask a counterfactual: if you used a similar period or a benchmark with the same risk, how much of this “skill” would remain?

A profitable outcome may certainly contain genuine skill, while also containing favorable conditions, leverage, and luck. A consistent audit standard is not meant to call every success accidental; it is meant to stop you from remembering uncertainty only when the result looks bad.

## Discipline: Do Not Ask Your Overheated Self to Become Smarter on the Spot

What these biases share is not that people do not understand the right principles. It is that emotions change how you interpret the same rules. Confirmation bias wants to move the success criteria; revenge trading wants to bypass loss limits; sunk costs want to grant an old project an endless extension; the gambler’s fallacy wants to rewrite a string of bad results as a reason to increase the next bet.

So psychological discipline should not be written merely as “stay calm.” It must become observable controls:

- Have someone who did not participate in building the model conduct an opposing review of the research results, so you are not both player and referee.
- Once a loss limit is triggered, have the system revoke permission to add risk instead of merely displaying a reminder that can be dismissed.
- Review whether a project continues using pre-agreed evidence and the next step’s information value, not by letting already-invested work hours vote.
- Any move to increase position size because of a winning or losing streak must have new evidence independent of that streak.

Chapter 11 provides risk rules and Chapter 13 provides their implementation through systems and governance; this chapter adds the human **attack model**. The objective is not to eliminate impulses, but to make sure that when an impulse appears, it lacks permission to change the rules.

## 📌 Chapter Takeaways

- Psychological biases do not make the system throw an error; instead, they generate a plausible-sounding explanation for changing the rules on the fly.
- **Confirmation bias** makes researchers collect only supporting evidence; use precommitments, opposing review, and change records to leave a trace whenever the goalposts move.
- **Revenge trading** mistakes “restoring the account balance” for the goal of trading; after a loss trigger, permission to add risk must be revoked, not merely warned against.
- **Sunk costs** let past investment hold future resources hostage; whether a project continues depends only on the evidence value of the next step, not on how long you have already spent.
- **The gambler's fallacy** treats winning and losing streaks as proof that the next trade should reverse; a string of outcomes can change a probability judgment only when combined with a mechanism and data.
- **Self-serving attribution bias** makes people credit profits to skill and blame losses on the environment; using the same advance standard and attribution audit for wins and losses is more reliable than intuition.

## ✍️ Try It / Think It Through

1. **Write the opposing case for your own strategy.** Do not repeat reasons that support it. Write only the three mechanisms most likely to make it fail, then identify which piece of evidence you would be most tempted to ignore. If you cannot write a single opposing argument, it usually does not mean the strategy is perfect; it means confirmation bias has taken over your pen.
2. **Design a friction that does not depend on willpower.** Assume that after a loss you are most likely to increase your position immediately. Write one specific control: who or what system revokes trading permission, how long before it can be restored, and which records must be reviewed before restoration. The point is not to choose a magic percentage; it is to make sure that, when the impulse appears, there is no direct path to changing the rules.

---

# Chapter 15: Negative Results Are Knowledge: Keep Improving Like a Scientist

## What Is a Crossed-Out Patch of Ocean Worth?

The previous chapters have made this point repeatedly: an idea that fails the test does not mean the research produced nothing. In this chapter, we will unpack that statement fully.

A navigator follows a particular route in search of an island and sees only open water after three weeks. They can crumple the chart, or write precisely: “On this route, in this season, and within this observation range, no island was found.” The second statement does not inflate “we did not see it this time” into “it never exists,” but it preserves the range already ruled out for those who come later. Negative results in quantitative research should be recorded the same way.

## The Value of a Credible Negative Result

Chapter 8 showed that the more attempts you make, the easier it becomes to select a positive-return curve from noise. A positive result therefore cannot be trusted merely because it looks attractive.

It may come from genuine alpha, or from selection bias, omitted costs, or random fluctuation. A negative result must not be exaggerated either; but if the design is reliable, it can at least identify which specifications and conditions were not supported.

“**Negative results are knowledge, not failure**” does not mean negative results are inherently nobler. It means that when a test has adequate power, reliable instruments, and clear decision boundaries, “not supported under these conditions” is reusable knowledge.

The gradually completed “chart” has practical value. Research time is limited; preserving negative results prevents you or your team from committing resources again to specifications that have already been tested and not supported.

## A Closing Note Cannot Say Only “Doesn't Work”

A credible finding of “not supported” still does not complete the case. If the record ends with only “doesn't work,” the boundary of knowledge has not been preserved.

For example, you have a hypothesis: “After Bitcoin falls sharply overnight, it usually rebounds over the next hour.” You run a backtest and find that it is unprofitable. So you write three words in your notebook: “Doesn’t work.” Then you turn the page and move on.

Those two words do not say what the test covered, what it did not cover, or what reusable conclusion remains.

A closing report should answer at least three questions:

- What exact statement was falsified? Was the whole claim, “sharp drops are followed by rebounds,” unsupported? Or only the “overnight” time window, while you have not tested daytime at all?
- What statement is still alive? Perhaps “rebounds after sharp drops” is thoroughly dead for coin A, but you have not even looked at coin B.
- What is the cheapest next step? Now that this path is blocked, where is the least costly branch to explore?

The same statement—“this strategy is unprofitable”—can become a small map once those three answers are added: which door is closed, which door has not yet been tried, and which door is most worth trying next.

## Four Cases Where You Have Not Actually Falsified Anything

Before writing “falsified” on the map, however, rule out four common misclassifications. Otherwise, the route crossed out may not be a dead end at all, but merely a test that was not done properly.

**Untested ≠ falsified.** Discarding an idea after only a few glances is not a negative result; it is an incomplete test.

**Insufficient statistical power ≠ ineffective.** Statistical power is the ability of a test to detect an effect under a given true effect size, noise level, and test design. The smaller the effect, the fewer the observations, and the greater the noise, the harder it is to move from “not observed” to “does not exist.”

**Instrument failure ≠ mechanism failure.** A data bug, look-ahead bias, or API truncation means the testing instrument is unreliable and cannot adjudicate the mechanism. Repair the instrument, then test again.

**Execution infeasibility ≠ the absence of a statistical effect.** This is the subtlest case. A repeatable price effect may exist in the data, yet net returns remain negative after accounting for spreads, slippage, and capacity. The accurate conclusion is: “It is not tradable under the current market, scale, and execution method.” It cannot be packaged as a profitable signal, but neither does it mean the statistical effect never appeared. If market structure or execution conditions change in the future, it can be retested under new specifications.

These four situations imply different conclusions and cannot all be abbreviated as “doesn't work.” A negative result has a clear boundary only when untested, insufficient power, instrument failure, and execution infeasibility are kept distinct.

## Deriving the Next Question from a Negative Result

A credible negative result not only closes one door; the reason for the failure may also narrow the next round's question.

Return to the earlier “rebound after a sharp drop” example. Suppose the overall test is not supported, but losses appear concentrated when the sharp drop coincides with unusually high volume. That observation can generate a new question: “Are sharp drops without a volume spike more likely to recover?”

But label it immediately as an **exploratory finding**. This condition emerged only after you saw the results; you cannot pretend afterward that the original hypothesis predicted it. It must be entered in the experiment ledger, with its mechanism and decision conditions written again, and then tested using data that did not participate in this observation. Otherwise, “finding a new direction through failure” can easily degenerate into the data snooping described in Chapter 8.

A negative result therefore does not automatically produce the right answer, but it may make the next question more precise. New conditions must be registered as exploratory hypotheses; they cannot be written afterward as something the original study had already predicted.

## Preserve the Verdict in a Research Log

The most direct way to preserve these boundaries and next questions is to keep a log.

Create a **research log** for yourself. It can be just a plain-text file. If this round is a confirmatory test, lock in the hypothesis, preregistered version, data range, and a complete set of specifications before you begin. If it is exploratory, first state the permitted scope of the search, and account for every variant you try. After the test is complete, add four things: the actual results, the proposition that did not receive support, the boundaries that remain untested, and the cheapest next experiment.

Preregistration locks in prior commitments; the research log preserves the later verdict. They are not duplicate descriptions in the same document: the first answers, “What did I originally bet on?” and the second answers, “What did the evidence ultimately change?”

Over time, the log becomes your own research chart. Six months later, you can confirm which questions were tested and why you stopped, and you will not repeat the same round of work simply because you forgot.

> **⚠️ Common Pitfalls**
>
>
> **“This strategy doesn't work. Delete it!”** If the rejected proposition and the still-untested boundaries are not recorded, deleting the code also deletes reusable information. A few months later, the team may commit resources to the same direction again.
>
>
> **“I tested it and found no effect, so the idea is wrong.”** First, check the four forms of false falsification. Did you truly test it, or merely glance at it (untested)? Was your sample large enough to detect the effect (statistical power)? Could the data or program be broken (instrument)? Could a statistical effect exist but be untradable at the current cost and scale (execution)? Until you rule out these four possibilities, what you have is not “falsification,” only “I did not see it this time.”

## 🔬 A Lesson from Practice: Stop, but Do Not Pronounce It Dead

The lab once studied a signal with a positive preliminary result. The data quality and mechanism explanation showed no obvious problem, and the team was preparing to move forward when it encountered a risk that could not yet be ruled out.

The available data could not determine whether the phenomenon held only in a particular market regime. That unknown was not enough to prove the signal wrong, but it was enough to prevent capital deployment.

The team therefore separated the capital decision from the knowledge verdict. Not one cent was deployed because risk X remained unresolved. The research log instead recorded: “The preliminary evidence remains worth preserving. If data Y become available, preregister a test that can distinguish between the two explanations.” This neither wrote the signal down as established nor treated the unresolved question as proof that the mechanism was dead.

Several months later, the required data became available. The team could continue testing from the coordinates preserved in the log instead of reconstructing why it had stopped.

The boundary left by the case is clear: deciding whether to take risk and deciding whether to preserve a lead for future testing are two different decisions.

## 📌 Chapter Takeaways

- **Negative results are knowledge, not failure.** But they must be written as bounded verdicts: what was not supported under which specifications, sample, and power. You cannot leap from not seeing something once to “it never exists.”
- Rejection does not complete the task. It is complete only when you can say precisely “which statement was falsified, which remains alive, and what the cheapest next experiment is.”
- Never confuse these four: untested ≠ falsified; insufficient statistical power ≠ ineffective; instrument failure ≠ mechanism failure; execution infeasibility ≠ the absence of a statistical effect.
- The counter-hypothesis can become material for the next round, but conditions that emerge after the fact count only as exploratory new hypotheses. They must be registered again and tested with new evidence.
- Separate decisions about money from decisions about knowledge: capital may stop because of unresolved risk, but research leads should not be carelessly pronounced dead merely because of unresolved questions.
- Keep a research log: record the hypothesis and preregistered version before starting; record the decision boundary and next step after finishing.

## ✍️ Try It / Think About It

1. **Write a closing report for a “failure.”** Find an idea you once abandoned—even something as simple as “I thought a moving average was very accurate, but it did not work when I tried it”—and write three lines in order: What exact statement did I falsify? What statement did I never test? If I started again, what would be the cheapest next step? Those three lines help determine what information the failure actually left behind.
2. **Review a conclusion that “the strategy doesn't work.”** Write one review question for each of the four false falsifications in this chapter. Whenever you encounter a negative result, use the checklist on your own research first, then on other people's conclusions.

---

# Chapter 16: Find Your Corner: Scale Matching, Capacity, and a Real Moat

Institutions hold clear advantages in capital, data, talent, and systems. A small-scale researcher who chooses the same problems—ones that depend on speed and scale—usually has no realistic chance of winning.

That does not mean small accounts have no room for research. The point is not to search for a mysterious corner that “institutions will never enter,” but to choose **problems that fit your scale, time, data, and execution conditions**, then assess capacity, costs, and competition honestly.

## Choose Problems That Fit Your Scale

Questions that require ultra-low latency, large-scale financing, expensive data, or complex access are often unsuitable for researchers with limited resources. Conversely, some opportunities have low capacity, or fixed research and operating costs that make them uneconomic for large pools of capital, yet may still be large enough for a small account.

Such questions do not belong exclusively to individual researchers, nor do they guarantee a return. A scale mismatch is only a screening clue; the idea must still survive tests of mechanism, data, costs, and out-of-sample evidence.

## Capacity: How Much Money an Opportunity Can Hold

**Capacity**, in plain language, is “how much capital a strategy can absorb before its expected net return materially deteriorates because of market impact, liquidity, and crowding.” It is not a permanent ceiling; capacity changes as markets, counterparties, and execution methods change.

Think of capacity as a small neighborhood noodle shop: a signature dish can be delicious and profitable with twenty tables, but that does not mean it will retain the same quality when ten thousand customers arrive tomorrow. Market opportunities work the same way. As capital grows, your own orders push up purchase prices and depress sale prices, and the market impact discussed in Chapter 10 begins to erode the marginal edge.

For a large fund, an opportunity whose capacity is only a tiny fraction of its assets may not cover the fixed costs of research, compliance, connectivity, and operations, even if its return rate is attractive. For a small account, the same capacity may be meaningful. This is simply a question of scale matching; it does not mean institutions cannot see it.

Therefore, **small scale can sometimes be a structural advantage.** Your orders are less likely to disturb the market, and you can study questions whose absolute profits are too small. But small scale also means weaker data, infrastructure, bargaining power, and diversification. It is a condition you can use, not a superpower.

## Obscurity and Difficulty: Possible Mismatches, Not Talismans

Beyond capacity, some subjects may be set aside because the data are messy, access is troublesome, the holding period does not fit organizational evaluation, or fixed costs are too high relative to profit.

What may genuinely create a mismatch is the **combination of difficulty and capacity**: spending three weeks cleaning data for an opportunity that cannot accommodate much capital may not be worthwhile for a large team, but it may be worthwhile for a small team willing to do detailed work. Conversely, popular markets do not necessarily lack opportunities, and obscure markets do not necessarily have tradable value.

That is why the lab prioritizes questions that fit its own resources: the mechanism makes sense, the data can be obtained, capacity is small but sufficient, and execution costs may be coverable. A scale mismatch tells you only **where to look**; it does not show that an advantage will persist. The second question is about the moat.

## A Moat Is Not a Single Technique

Here, a **moat** means a set of conditions that is difficult to replicate and can extend the life of an advantage. It rarely comes from a clever idea, a faster machine, or a complicated formula alone.

Recall the practices this book has taught throughout: lock specifications before confirmatory tests; honestly account for every variant explored; subject attractive Sharpe ratios to audits for selection bias and distribution shape; use calibrated adverse scenarios in execution models; do not upgrade conclusions before out-of-sample evidence appears.

These checks will reduce confidence in some attractive results, but they also prevent the same false positive from repeatedly consuming time and principal. Rigor does not create excess returns. Its role is to reduce misjudgments, preserve reusable knowledge, and keep execution and risk controls faithful to the research conclusion. A real moat often combines data or access, understanding of mechanisms, capacity mismatches, execution details, and discipline.

## Make Your Research Capability Operational First

After finding a potentially suitable corner, there is still no need to rush into testing it with principal. Signals that genuinely deserve further validation are uncommon, and some decay as competition and market conditions change. If you wait until a signal appears before building a backtesting environment, adding risk rules, and cleaning data, the research is likely to be rushed and execution risk will rise.

Before deploying important capital, establish a trustworthy backtesting process, a set of approved risk boundaries that cannot be loosened on the fly, and fixed procedures for cleaning data and reconciling accounts.

These preparations cannot guarantee that you will capture an opportunity, but they allow a new hypothesis to be tested promptly and reproducibly. Capability comes before opportunity precisely so that haste does not manufacture a new source of risk.

## Make Both Curiosity and Discipline Habits

Research needs both curiosity and discipline. **Curiosity** proposes questions; **discipline** decides which questions deserve to continue, which results can only be classified as noise, and which risks must not enter a real-money account. Without discipline, research keeps chasing bright spots. Without curiosity, even the most rigorous process has no new question to test.

Neither can depend only on how you feel that day. Discipline must become the risk boundaries, approvals, and monitoring of Chapters 11 and 13. Curiosity needs a regular research rhythm: collect questions at set intervals, advance only one decidable experiment at a time, and write the result in the log. In this way, negative results will not drive you out of research, and attractive results cannot make you skip the gates.

A truly sustainable state is not permanent excitement. It is knowing what to do next regardless of whether this round goes well, while also knowing which steps must never be taken.

## A Farewell Roadmap: The Next Three Steps

The preceding ideas—scale matching, research capability, and discipline—can be turned into a practical route that begins with three steps.

**Step One: Control the downside first.**

Do not rush to make money. First practice connectivity, monitoring, and circuit breakers in a simulated environment. Then enter at the minimum executable scale through the governance chain in Chapter 13. Position size, loss boundaries, and conditions for scaling up should all follow the rules already approved in Chapter 11. The goal of this step is not to prove the system is forever safe. It is to use fault injection and reconciliation to confirm that in anticipated bad scenarios, it stops, alerts, and does not expand risk on its own.

**Step Two: Choose a problem that fits you, and honestly complete one research project.**

Choose one small question you are genuinely curious about, whose mechanism makes sense, and whose data, time horizon, capacity, and execution conditions all match your resources. Choose only one, and complete the full cycle in the order of Chapters 6 through 10: write down the hypothesis and decision conditions, lock the confirmatory specifications, backtest, perform statistical checks, and then account for costs. The point is not to win on the first try, but to obtain a verdict that can withstand review.

**Step Three: Turn the research cycle into a habit.**

Then do it again. Write each verdict in the research log: what was rejected, what remains untested, and what the cheapest next experiment is. What you accumulate is not a résumé that says “tried many things,” but a record of judgment that will not repeatedly step into the same pit.

None of these three steps requires you to become smarter, faster, or richer than institutions first. They require a different, more controllable advantage: choose problems that fit, test honestly, and hold the risk boundaries.

Find one small question worth answering seriously, complete the work, preserve the conclusion, and then move to the next one.

> **⚠️ Common Pitfalls**
>
>
> **Pitfall One: Thinking that winning requires defeating large institutions head-on in speed and scale.**
> You do not need to choose a battlefield where you are structurally disadvantaged. A more practical approach is to find questions that match your scale, horizon, data, and execution capabilities. But do not conclude that institutions are completely absent because of this; every positive result still needs to withstand tests of competition, capacity, and costs.
>
>
> **Pitfall Two: Assuming anything “obscure” is an opportunity.**
> Obscurity is neither necessary nor sufficient. Popular markets may contain risk premia or opportunities at different horizons; obscure corners may simply have no liquidity and no mechanism. Obscurity is at most a clue. What determines whether something is worth continuing remains the mechanism, evidence, net return, and capacity.

## 📌 Chapter Takeaways

- Do not choose a battlefield where you are structurally disadvantaged in speed and scale; prioritize questions that fit your capital, horizon, data, and execution capabilities.
- Small scale can sometimes reduce market impact and accommodate low-capacity questions, but it also comes with weaker infrastructure and diversification.
- Rigor does not create alpha; it reduces false positives, preserves knowledge, and prevents data, execution, and risk from betraying the research.
- A real moat usually comes from a combination of mechanisms, data or access, capacity mismatches, execution details, and discipline.
- Capability comes before opportunity: make data, backtesting, risk boundaries, and deployment governance into reliable processes first.
- The next three steps: control the downside first → choose a matching problem and honestly complete the research → turn the research cycle into a habit.

## ✍️ Try It / Think About It

1. **Draw three candidate questions.** Take a sheet of paper and write down three topics that may fit your scale and capabilities. For each one, answer five questions: Who might be paying this money? Why would the mechanism persist? Can the data be obtained from the point-in-time perspective? What remains after costs? Is the capacity enough for you, and at what scale will it decay? If you cannot answer two or three of them, it is not yet a niche—only a name.
2. **Inspect your research habits.** Between proposing new questions and following testing discipline, which one are you more likely to neglect? For the weaker one, design **one** specific rule—for example, “Before acting on any idea, write down one falsification condition,” or “Every month, seriously test at least one new question that is allowed to fail.” Write the rule on the first page of your research log.

---

# Conclusion: The Tools of a Pessimist, the Heart of an Optimist

Do you remember opening the first page and perhaps expecting a profitable path you could copy? This book has not offered a guaranteed indicator or a fixed set of entry and exit points. What it aims to leave you with is a set of research principles: **the tools of a pessimist, the heart of an optimist.**

Apply pessimism to your method. Data may be wrong; a backtest may peek into the future; attractive results may simply mean that you tried enough things; execution may be worse than the model. Build these doubts into the process. Make conclusions able to withstand attacks from the opposing side, and allow real money to move only within pre-approved boundaries.

Reserve optimism for continuing the research. Having an idea rejected does not mean you are unsuited to research; it only means this specification was not supported. Record the boundaries clearly, ask the next cheaper, more precise question, and you are not standing still.

Do not rely only on “I have thought it through.” Risk boundaries must be written into the system so that excitement cannot loosen the rules on the fly. Research decisions must be written into the log so that a negative result is not discarded together with the knowledge already gained.

After closing the book, you can do one small exercise: write down the date and a hypothesis you care about, then add one sentence—“What result would make me admit that this time was not supported?” Do not look at the data first. The exercise will not directly generate a return, but it gives the next judgment a clear decision rule.

Ahead there is no crystal ball and no holy grail; only a map that evidence will gradually make more accurate. “The tools of a pessimist, the heart of an optimist” means being strict enough in the face of evidence while remaining willing, after repeated rejections, to pose the next testable question.

---

# Appendix A: A Short Glossary of Quantitative Terms

This glossary collects the core terms used in the main text, organized into seven groups by topic. Each entry first gives a plain-language definition suitable for beginners, then adds the boundary most often misstated. It is the book's terminology authority: where the main text uses an abbreviation or metaphor, the preferred term and meaning here govern.

Definitions have been compressed for introductory purposes; they are not complete legal, exchange, or statistical standards. In a specific market, the relevant contracts, fees, and rules still control.

## I. Markets and Trading

### Trading Approaches and Risk Exposure

- **Quantitative trading** — Trading that uses data, statistics, or mathematical models to support research and decisions. It is often systematic, but the two are not exact synonyms: a quantitative process may retain human judgment.
- **Systematic trading** — Trading that expresses entries, exits, positions, and execution as repeatable rules. The rules can be simple and need not use complex models.
- **Discretionary trading** — Judgment by a trader based on experience and current information. It does not mean arbitrary trading, but when rules are not fully specified, it is harder to backtest, reproduce, and audit.
- **Strategy** — A complete executable design that includes at least the instruments traded, signals, positions, exits, cost assumptions, and risk boundaries. A signal is only one component.
- **Long** — Risk exposure that benefits when price rises. In spot markets it usually means buying before selling; derivatives can also create a long position.
- **Short** — Risk exposure that benefits when price falls. It can be created by borrowing and selling, or through derivatives such as futures and options; costs and risks differ by instrument.
- **Leverage** — Economic risk exposure greater than the capital actually committed. It may arise from borrowing or derivatives and amplifies gains, losses, and forced-liquidation risk alike.
- **Margin** — Funds or assets pledged to maintain a leveraged position. Adverse markets may require additional margin; if it is insufficient, the platform may reduce or liquidate positions under its rules.
- **Liquidation / forced liquidation** — A position being forcibly closed because margin is insufficient or platform risk rules are triggered. The execution price may be poor, and remaining principal is not guaranteed to be intact.

### Market Data and Common Measures

- **Candlestick / OHLC** — A summary of a period's market activity using open, high, low, and close prices. It is a compressed summary and does not contain the full sequence of trades within that period.
- **Volume** — The quantity or value actually traded during a period. High volume does not automatically mean good liquidity; spread, depth, and executable size still require separate checks.
- **Volatility** — The magnitude of changes in returns. It is one measure of risk, not all risk; gaps, liquidity, and tail losses may not be adequately reflected.
- **Return / annualized return** — Profit or loss as a proportion of capital or price; annualization converts it to one year according to an agreed method. Frequency, compounding convention, and sample length affect comparability.
- **Moving average** — A moving average of prices over recent periods, used to smooth short-term fluctuation. It is a descriptive tool, not an inherent predictor.
- **Moving average crossover** — A class of rules that produces signals from crossings of short- and long-term moving averages. The text uses it to illustrate rule formalization, not to recommend any particular number of days as an effective strategy.

### Order Books and Microstructure

- **Order book** — Visible limit buy and sell orders arranged by price. Hidden orders, off-book intent, and resting orders that may be cancelled at any time may not appear in it.
- **Depth** — The visible quantity resting at each price level. Visible depth changes and can be cancelled; it cannot be treated as inventory guaranteed to be executable.
- **Bid-ask spread / spread** — The difference between the best ask and best bid. When immediate execution is required, crossing the spread is usually a cost.
- **Liquidity** — The ability to trade a given size within a limited time without imposing excessive cost. It involves spread, depth, execution speed, resilience, and market state.
- **Limit order** — An order that specifies the worst acceptable price. It guarantees a price boundary, not execution; if the price crosses the book, a limit order may execute immediately and become a taker order.
- **Market order** — An order that prioritizes prompt execution without a price ceiling or floor. It may be partially filled, rejected, or receive a very poor price in extreme conditions, so it is not an unconditional guarantee of execution.
- **Maker** — Under exchange classification rules, the party whose order first enters the order book and adds liquidity. Maker is a fee and matching identity, not a synonym for a professional market maker.
- **Taker** — The party whose order immediately trades with existing resting orders and removes liquidity. Market orders are usually takers; immediately executable limit orders can also be takers.
- **Market impact** — The way your own order changes executable prices or subsequent quotes. It varies with size, speed, depth, and market state, and is one source of slippage.
- **Slippage** — The difference between the actual execution price and a benchmark price selected in advance. The benchmark must be specified; network delay, market movement, partial fills, and market impact can all cause slippage. A complete non-fill should instead be recorded as a non-fill and opportunity cost.
- **Market microstructure** — The field studying how orders enter, queue, match, cancel, and form prices. It explains why a “screen price” is not the same as your actual execution.

### Transaction Costs

- **Transaction cost** — All friction paid to establish, adjust, and exit positions, including fees, spread, and slippage, plus market-dependent taxes, stock-borrow fees, funding rates, financing, and infrastructure costs.
- **Commission / fee** — A charge levied by a broker, exchange, clearing firm, or platform. It may be calculated as a fixed amount, a percentage of trade value, by tier, or by maker/taker identity.
- **Turnover** — Trading value over a period relative to portfolio size. It measures how much risk exposure was traded, not merely the number of orders.
- **Gross return** — Strategy return before trading, financing, and related costs are deducted.
- **Net return** — Return after relevant costs are deducted on the same basis. Whether a strategy can be traded should be assessed primarily from net, not gross, results.
- **Negative-sum game** — In a closed trading comparison where gains and losses mainly transfer among participants, costs make aggregate results lower than before costs. It does not mean that all long-term investment, corporate value creation, or overall market returns must be negative.

### Market Efficiency and Opportunity

- **Efficient Market Hypothesis (EMH)** — A family of hypotheses about the degree to which prices reflect available information. It does not claim prices are always correct; it reminds you that public, obvious, low-cost excess returns are difficult to retain for long.
- **Alpha / excess return** — Return remaining relative to a defined benchmark after controlling for relevant risk exposure. Observing positive alpha does not automatically prove skill; estimation error, selection bias, and costs still require audit.
- **Smart money** — A colloquial label for professional, well-informed, or execution-capable participants. The label does not guarantee that they are always right and cannot replace analysis of a specific mechanism.
- **Arbitrage** — Locking in, or nearly locking in, a price difference with offsetting positions; under the ideal definition it is nearly risk-free after costs. Many uses of “arbitrage” in market speech are actually relative-value trades and still have basis, financing, execution, and tail risks.
- **Market anomaly** — A phenomenon that conflicts with a benchmark model or simple efficiency explanation and repeatedly appears in data. It may arise from risk compensation, behavior, institutions, data problems, or decay after competition; it is not automatically tradable alpha.

## II. Data

- **Garbage in, garbage out** — If input data are wrong, even a precise model will process the error into something that looks more like an answer.
- **Timestamp** — A label recording when an event occurred, was published, was received, or was stored. Different time meanings cannot be mixed; time zones must also be unified.
- **Point-in-time** — Returning to a historical decision time and using only versions and membership lists that were available then. Data revised later cannot be fed back into the past.
- **Look-ahead bias** — A decision uses information that was unknowable at the time, or reverses the ordering of signal, order, and fill. It often makes a backtest falsely attractive.
- **Survivorship bias** — A sample retains only instruments, funds, or accounts that still existed later, omitting delisted, closed, and failed cases and thereby systematically flattering historical results.
- **Silent failure** — A system does not explicitly error but has stopped updating, become misaligned, dropped data, or otherwise departed from expectation. It requires reconciliation, coverage, and freshness checks to find proactively.

## III. Research Methods

- **Hypothesis** — A proposition that data or observations can test, such as “when condition A appears, how does the distribution of future returns change?”
- **Assumption** — A premise on which a model, mechanism, or calculation depends, such as “execution costs are approximately stable at this size.” An assumption is not the primary proposition being tested, but a wrong assumption changes the conclusion.
- **Falsifiability** — A proposition has, in principle, observations that conflict with it. A claim that can be explained as right no matter what happens cannot produce a clear research decision.
- **Falsification** — Finding, using pre-specified evidentiary standards, that a precise proposition is not supported. It does not automatically prove the opposite proposition, nor can it condemn untested variants with it.
- **Falsification contract** — Decision conditions written before viewing results: what to measure, what counts as not supported, and which boundaries are outside this round's scope. It prevents moving the goalposts after the fact.
- **Mechanism hypothesis** — An economic, behavioral, or institutional explanation for why a phenomenon exists. A mechanism can improve extrapolation credibility and help design disconfirming tests, but a plausible story is not proof.
- **Research loop** — The process of posing a question, preparing data, defining a specification, backtesting, performing statistical audit, checking costs and risks, reaching a decision, and registering the next question for the next round.
- **Backtest / backtesting** — Simulating a strategy on historical data in executable time order. It is useful for rough screening and comparison, but does not guarantee future performance or real execution.
- **Pessimistic or conservative fill model** — First establish an explainable baseline fill model, then test results under adverse and stress scenarios supported by data. It is not arbitrarily setting costs to an extreme, and it must not double-count spread and slippage.
- **In-sample** — Data used for exploration, modeling, and selecting specifications. Trial and error are permitted here, but every attempt must be accounted for.
- **Out-of-sample** — Data not involved in current model selection and used to test extrapolation. Repeatedly changing rules in response to it gradually strips it of out-of-sample status; it is not a magic exam that remains valid forever.
- **Signal** — A strategy's numerical expression of future direction or relative strength. It may mean long, short, or no action; it may also be a continuous score, probability, or ranking.
- **Factor** — A systematic variable or exposure used to explain or predict common return differences across assets. Factors can often form portfolios and be tested across instruments.
- **Feature** — An observable variable input to a model. A feature may be only an engineering input and need not have a factor's economic meaning, cross-sectional structure, or tradable exposure.
- **Parameter** — A number that must be set or estimated in a rule or model. Confirmatory tests should freeze the complete specification; exploring multiple parameters is allowed, but every variant must enter the experiment ledger.
- **Robustness check** — Whether a conclusion broadly holds after changing reasonable neighborhoods, samples, definitions, or implementations. Robustness is not proof, and a single-point optimum is not automatic fraud.
- **Ablation** — Removing or replacing one component to observe its incremental contribution. Components can interact, so “no difference when removed” must also be interpreted alongside joint tests.
- **Control / benchmark** — The reference against which a strategy is compared. A good benchmark matches the primary risk, holding period, and cost rather than deliberately choosing a weak opponent that must lose.
- **Curve fitting** — Continually adding degrees of freedom to fit data already seen. Fitting itself is a modeling tool; the problem is treating sample noise as an extrapolatable pattern.
- **Research log** — A record preserving the prior specification, all exploratory variants, data versions, code versions, results, decision boundaries, and next questions. It makes negative results reusable and leaves evidence of later changes of story.

## IV. Statistical Rigor

- **Overfitting** — A model learns accidental details in its sample too thoroughly, producing attractive in-sample results that fail on new data. Degrees of freedom, number of selections, and sample information jointly determine the risk; it is not that “complex models are inherently guilty.”
- **Multiple testing** — When many tests are conducted in the same research family, the chance of at least one accidental good result rises. Correlated tests are not independent, but they still need unified accounting and adjustment.
- **Data snooping** — Repeatedly examining the same data, changing conditions based on results, and finally reporting only the most attractive version. Exploration itself is not wrong; presenting exploratory results as prior confirmation is.
- **Conditional return / subgroup analysis** — A result calculated only for a particular period, state, or subsample. Every data-driven slice increases selection freedom and should enter the same research family; such slices are usually not independent trials.
- **Statistical power** — A test's ability to identify an effect, given the true effect size, noise, sample, and test method. When power is low, “not significant” cannot simply be translated as “no effect.”
- **Significance level** — The long-run proportion of false positives permitted for a single test when the null hypothesis and testing conditions hold. Five percent does not mean “there is a 95% chance the result is true,” nor does it mean it is profitable.
- **Equity curve** — The path of account or strategy equity over time. An attractive curve is a description, not independent evidence; random processes can also produce smooth upward paths.
- **False green** — Tests report that everything passes, while critical behavior was not covered or the program did nothing at all. Validation must include negative tests that deliberately trigger failure.
- **Preregistration** — Locking the hypothesis, specification, primary metrics, and decision rules before a confirmatory test. It does not prohibit exploration; it requires a clear separation between exploration and confirmation.
- **Sharpe ratio** — Generally, average excess return divided by return volatility, often annualized. It does not fully describe skewness, tails, liquidity, or maximum drawdown, and is affected by sample length and serial correlation.
- **Deflated Sharpe Ratio (DSR)** — A statistical adjustment that considers strategy selection, multiple trials, and factors such as skewness and kurtosis of the return distribution when interpreting an observed Sharpe ratio. It is not simply dividing Sharpe by the number of trials, and it cannot replace independent validation.

## V. Risk, Capital, and Portfolios

- **Position** — Directional risk exposure to an instrument or strategy, expressible in units, notional value, or risk units; it is not merely “how much money was spent.”
- **Position sizing** — The process of translating a risk budget, exit distance, volatility, liquidity, leverage, and portfolio exposure into an actual position.
- **Risk budget** — Risk that is allocated in advance and acceptable for a trade, strategy, asset, or entire portfolio. It is a boundary, not a profit target.
- **Stop loss** — A pre-defined exit or risk-reduction condition, which may be based on price, time, volatility, or hypothesis failure. It constrains decisions but does not guarantee execution at the trigger price.
- **Maximum drawdown** — The largest decline from a historical peak to a subsequent trough in a given equity path. It depends on the sample and path; it is not an upper bound on future worst loss.
- **Circuit breaker** — A rule that stops adding risk and enters review when loss, anomaly, or another risk metric reaches an approved boundary. Specific thresholds should be set for the strategy and account; percentages in this book are examples only.
- **Ad hoc averaging down / adding after losses** — Temporarily increasing risk or moving exit conditions after a loss and reluctance to accept it, when the original specification did not require this. It differs from pre-registered staged entry or rebalancing with a total risk cap.
- **Martingale betting** — Increasing bets in an escalating sequence after losses in an attempt to cover prior losses with the next gain. It cannot turn negative expectancy positive; it concentrates risk into a few enormous tail losses, and limited capital and trading constraints make it unsustainable.
- **Compounding** — Returns participating in subsequent investment, causing capital to change along a multiplicative path. Deep losses shrink the base, so recovering requires a return greater than the original loss percentage.
- **Correlation** — The degree to which two return series move together in a linear sense, usually between -1 and +1. Zero does not mean independence, and correlation changes with frequency, window, and market state.
- **Covariance** — A quantity combining the direction of co-movement of two returns with their respective scales. Portfolio risk and risk-contribution calculations usually rely on a covariance matrix.
- **Diversification** — Combining different sources of risk to reduce dependence on a single member or mechanism. It cannot guarantee no loss, and protection can weaken in stressed periods.
- **Equal weight** — Allocation giving each member the same capital weight. It is a valuable simple benchmark, but does not guarantee balanced risk or suitability for every account.
- **Risk parity** — Seeking to make members' contributions to portfolio risk more balanced. Full calculation must consider covariance and check rebalancing costs, leverage, financing, and tail risk.
- **Portfolio-level** — Looking at risk, cost, and constraints across all positions together. Individual strategies being safe does not mean that several correlated strategies remain safe when combined.
- **Capacity** — The amount of capital a strategy can deploy before expected net returns are materially eroded by market impact, liquidity, and crowding. Capacity changes with markets and execution.

## VI. Mindset and Research Behavior

- **Confirmation bias** — Being more permissive toward evidence supporting one's view and more demanding toward opposing evidence, allowing the same proposition to escape decision indefinitely.
- **Revenge trading** — Departing from original rules or expanding discretion or position size in order to “make back” losses quickly. Past account losses are not a new mechanism for the next trade.
- **Sunk cost fallacy** — Continuing to put future resources into a low-value project because one cannot bear to abandon unrecoverable past investment. Whether to continue should depend on future expected value.
- **Gambler's fallacy** — Believing, without new evidence of a mechanism, that a streak of wins or losses must be offset by the next outcome. Markets may have dependent structures, but one's own loss sequence does not raise the win probability of the next trade.
- **Self-serving attribution bias** — Attributing good results to ability and bad results to environment or luck. Wins and losses should receive the same pre-specified standards and attribution audit.
- **Moat** — A combination of conditions that makes an advantage hard to copy or erode, possibly including data, access, mechanism, capacity, execution, and organizational discipline. Rigor is a foundation; it does not create alpha by itself.

## VII. Governance and Live Execution

- **Governance chain / governance** — A set of responsibilities and controls from research to live trading specifying who can approve what, what evidence is required, and when activity must stop or escalate to review.
- **Gate** — A strategy may enter the next stage only after reaching pre-written graduation conditions. A gate should retain version, evidence, and approval records.
- **Paper trading** — Simulating orders with live market data without taking real profit and loss. It is suitable for validating plumbing and process, but cannot fully reproduce queue position, market impact, or psychological pressure.
- **Fail-closed (default to closed in risk-critical states)** — When critical conditions such as stale data, unreconciled positions, or unclear permissions are abnormal, the system by default stops adding risk or rejects expansion. Non-critical alerts may be downgraded; critical states must be defined in advance.
- **Human-in-the-loop** — Humans approve transitions to live trading, capital, risk limits, permissions, and core strategy changes; machines may automatically execute routine orders within approved boundaries. It does not mean every automated order must be clicked manually.
- **Monitoring and reconciliation** — Checking data, positions, orders, fills, and profit and loss on the strategy's risk clock, and reconciling internal records with broker or exchange records. Merely seeing that the program is “alive” is insufficient.
- **Kill switch** — Once triggered, stops adding risk, cancels cancellable orders, and attempts to reduce or close positions according to the plan. It does not guarantee instant full liquidation during outages, gaps, or liquidity droughts.
- **API key** — A credential allowing a program to access a trading account. Use secret management, least privilege, live/demo separation, rotation, and revocation; trading programs normally should not have withdrawal permission.

---

# Appendix B: Beginner Checklists and Further Reading

This appendix deliberately retains **intentional repetition**. The main text explains why; the checklists simply place the actions easiest to miss back in front of you when you are excited, tired, or rushed.

No item is a guarantee that checking it makes you safe. It is more like a pre-flight checklist: it cannot judge the weather for you, but it can keep you from having an accident because you forgot to close the cabin door. If any item has no answer, the default action is not to force a “yes,” but to stop and gather evidence.

## Checklist 1: Before Starting Research (Chapters 5, 6, and 8)

### A. State what this round is actually doing

- [ ] I have labeled this round **exploratory** or **confirmatory**. Exploration may find directions; confirmation tests a proposition already locked down.
- [ ] The hypothesis can be stated in one sentence: what information is visible when, what condition does it trigger, which future interval does it predict, and what are the direction and metric?
- [ ] I have written at least one plausible mechanism and two alternative explanations that could produce the same phenomenon.
- [ ] Decision conditions were written before viewing results: what counts as not supported, and which boundaries does this round not test at all?
- [ ] If this is a confirmatory test, the complete specification, primary metrics, and decision rules have been preregistered; if exploratory, the permitted search range and every variant will enter the log.
- [ ] I distinguish “statistically detectable” from “economically worth trading”: even if the effect exists, is it large enough to cover costs and risks?

### B. Then interrogate the data

- [ ] For every field, I distinguish **event time, publication time, and the time I could actually obtain it**, and have not inserted numbers published later into the past.
- [ ] The instrument universe, index constituents, financial-statement revisions, and delisted samples are all retained **point-in-time**, rather than keeping only members that survived later.
- [ ] Time zones, trading days, daylight saving time, timestamp meanings, and data frequencies have been standardized.
- [ ] Gaps, duplicates, outliers, pagination limits, lookback limits, and API truncation have been actively checked, rather than merely checking whether the program errored.
- [ ] After writing data, I have read it back and verified coverage, confirming that downstream processes can actually retrieve it at the right time.
- [ ] I can state what this data **does not cover**. Without knowing the boundary of missingness, I cannot call it a complete sample.

## Checklist 2: During Backtesting and Statistical Audit (Chapters 7, 8, 9, and 10)

### A. Time order and research specification

- [ ] I have reviewed observation, signal, order, and fill times one by one; I did not first see the full result within the same candlestick and then pretend I had already traded.
- [ ] All explored parameters, filters, time windows, and instrument subsets enter one research ledger; I did not retain only the winners.
- [ ] The confirmatory specification is frozen; any modification after seeing results is marked as a new version rather than rewritten as the original plan.
- [ ] In-sample and out-of-sample data are split in chronological order, and I record whether out-of-sample data have been repeatedly viewed. Data used to change rules no longer pretend to be purely out-of-sample.
- [ ] Results do not survive only at a sharp single point across parameter neighborhoods, different market states, and reasonable definition changes.
- [ ] Ablations and controls use matched risk, holding-period, and cost conventions; the complex strategy genuinely adds auditable value beyond a simple benchmark.

### B. Statistical honesty

- [ ] I have defined the research family in advance: which strategies, parameters, and conditional slices belong to the same batch of attempts?
- [ ] Conditional returns and after-the-fact groupings are not treated as free discoveries; correlated slices are not independent, but still count in the selection process.
- [ ] I report not only “significant/not significant,” but also effect size, sample uncertainty, and the size of effect that current power can exclude.
- [ ] I disclose the Sharpe ratio's sample length, serial correlation, skewness, and tail risk, rather than treating one number as a complete risk profile.
- [ ] If I selected the best result from many candidates, I have used appropriate multiple-testing adjustment, DSR, or fresh data confirmation to reduce selection bias.
- [ ] I treat a beautiful curve only as a description, not as independent evidence.

### C. Costs, execution, and capacity

- [ ] The fill benchmark is clear: mid-price, arrival price, opening/closing auction, or another benchmark; the strategy truly had a route to obtain it then.
- [ ] Fees, spread, slippage, financing, stock borrow, funding rates, and taxes are included as required by the market, and I have checked that none are double-counted.
- [ ] Turnover is calculated as traded value relative to portfolio size, rather than merely counting orders or “round trips.”
- [ ] Baseline, adverse, and stress cost scenarios all have support from historical fills or market structure; I have neither made optimistic wishes nor substituted impossible extreme penalties for modeling.
- [ ] Non-fills, partial fills, and opportunity costs are recorded separately rather than all stuffed into one vague slippage number.
- [ ] After scaling size, I have re-estimated market impact and capacity rather than assuming small-size results can be copied linearly to large size.

### D. Prevent “false green”

- [ ] I have deliberately supplied bad timestamps, missing fields, duplicate orders, and out-of-bound positions, confirming that the system fails where it should fail.
- [ ] Tests check not only “no error,” but also whether trade count, positions, profit and loss, rejected orders, and risk state match expectations.
- [ ] Critical calculations have an independent implementation, hand-worked example, or invariant for cross-checking; I do not trust an entire chain to the same possibly wrong code.
- [ ] A green backtest earns only eligibility for controlled validation, not a license for live trading.

## Checklist 3: Before Touching Real Money and Scaling (Chapters 11, 12, 13, and 14)

### A. Risk boundaries before opportunity

- [ ] Risk limits per trade, strategy, asset, day, and portfolio derive from account capacity and strategy distributions, rather than copying the book's 1% or 5% examples.
- [ ] Position calculations leave room for gaps, widening spreads, rejected orders, leverage, and correlated positions being hurt together.
- [ ] Exit conditions are clear, including what to do if execution cannot occur at the planned price after a trigger. I do not treat a stop loss as an execution guarantee.
- [ ] Any staged entry is registered before entry and total risk is capped; after losses I may not temporarily increase size to average down or move the exit line.
- [ ] Martingale-style escalating positions are explicitly prohibited; a string of high win rates will not conceal tail bankruptcy risk.
- [ ] The portfolio has been stress-tested for common shocks, rising correlations, and liquidity droughts, rather than only checking each strategy in isolation.

### B. Phased deployment

- [ ] Paper trading first validates market data, clocks, order state, rejected orders, reconnection, monitoring, and risk rules; it does not use fake fills to prove profitability.
- [ ] Real money begins at the **smallest executable size**: large enough to produce real friction, yet small enough that validation failure does not cause material harm.
- [ ] Small live trading is reconciled trade by trade against the backtest: fill deviations, partial fills, non-fills, fees, and exceptional retries are all recorded.
- [ ] Every scale-up has quantitative graduation conditions; after changing size, instruments, leverage, or frequency, I re-estimate costs, capacity, and risk.

### C. Governance and change control

- [ ] Risk-critical states are specified; when data are stale, positions do not reconcile, or permissions are unclear, the default is to stop adding risk or reject expansion.
- [ ] Humans approve transitions to live trading, capital, risk limits, permissions, core strategies, and scale-ups; routine orders execute automatically only within approved boundaries.
- [ ] Every deployment has a version, approver, evidence package, and rollback plan; no parameters are changed ad hoc in production without a trace.
- [ ] Once a boundary is triggered, resuming trading requires independent review; the same impulse that just triggered the circuit breaker cannot decide to lift it with one click.

### D. Monitoring, security, and emergency stop

- [ ] Monitoring displays data freshness, positions, orders, fills, profit and loss, and distance from risk boundaries on the strategy's risk clock; exceptions can be escalated promptly to an owner.
- [ ] Internal positions, orders, and fills are reconciled regularly with the broker or exchange; retried orders use unique identifiers to avoid executing the same intent twice.
- [ ] The kill switch has been rehearsed: it stops adding risk, cancels cancellable orders, and reduces risk according to the plan; I also understand that it does not guarantee instant full liquidation in every market.
- [ ] API keys are in a secret-management system, live and demo are separated, and least privilege, rotation, and revocation are used; the trading program has no unnecessary withdrawal permission.
- [ ] The runbook specifies separate degradation and human-takeover steps for exchange outages, network interruption, market-data-source failure, and local-system disconnection.

## The Ten Mistakes Beginners Make Most Often (Quick Reference)

1. **Looking at data before writing the hypothesis.** Deciding what you meant to test only after seeing the results disguises exploration as prediction. (Chapters 6 and 8)
2. **Time travel.** Reversing the order of signal, order, and fill, or using data that were unpublished then or only revised later. (Chapters 5 and 7)
3. **Keeping only survivors.** Looking back using today's still-trading list while removing delisted, closed, and failed samples from the denominator. (Chapters 2 and 5)
4. **Failing to account for exploration.** Trying many parameters and conditions, submitting only the best report card, and then calling it the “original strategy.” (Chapters 8 and 9)
5. **Treating significance as truth and tradability.** Ignoring multiple testing, statistical power, effect size, and net returns. (Chapters 8, 10, and 15)
6. **Confusing cost conventions.** Omitting financing and slippage, or putting spread into slippage and deducting it again; counting trades instead of turnover value. (Chapters 4 and 10)
7. **Believing false green.** All tests pass, but no failure was deliberately triggered and no one checked that the system placed the orders it should and rejected the risks it should. (Chapters 7 and 13)
8. **Treating stops as guarantees and exceptions as courage.** Ignoring gaps and liquidity, then loosening boundaries after a trigger because “this time is different.” (Chapters 11 and 14)
9. **Temporarily expanding risk after losses.** Unregistered averaging down, moving exit lines, and martingale practices hide tail losses behind a string of small wins. (Chapter 11)
10. **Jumping straight from backtest to large automated trading.** Skipping minimum-size live runs, reconciliation, permission separation, and kill-switch drills leaves capital to discover engineering problems. (Chapter 13)

> There is one more error, unnumbered but most invisible: **treating “being busy” as “making progress.”** The story of 115 code commits and zero real experiments reminds you that volume of activity is not an increment of knowledge. The daily question should be “How many reviewable conclusions did I add?” not “How much did I do?” (Chapter 3)

## Further Reading: Follow the Problem

The following are entry points by topic, not a reading list that makes you profitable upon completion. Read one or two most directly relevant to your current problem first, and verify the edition and translation you actually have.

**I. Randomness, judgment, and tail risk**

- Nassim Nicholas Taleb, *Fooled by Randomness* and *The Black Swan*.
- Daniel Kahneman, *Thinking, Fast and Slow*.

Why read: to help distinguish luck, sample selection, overconfidence, and tail events; relevant to Chapters 2, 8, and 14.

**II. The complete process of systematic trading**

- Ernest P. Chan, *Quantitative Trading*, *Algorithmic Trading*.
- Robert Carver, *Systematic Trading*.
- Andreas F. Clenow, *Following the Trend*.
- Perry J. Kaufman, *Trading Systems and Methods*.

Why read: to see how a system is fully specified, from rules and positions to costs and execution; relevant to Chapters 1, 3, 9, 11, and 13.

**III. Backtest overfitting and statistical testing**

- David Aronson, *Evidence-Based Technical Analysis*.
- Papers by David H. Bailey, Jonathan Borwein, Marcos López de Prado, and others on the probability of backtest overfitting and the Deflated Sharpe Ratio.
- Marcos López de Prado, *Advances in Financial Machine Learning*.

Why read: to deepen understanding of multiple testing, strategy-selection bias, DSR, and the distinctive statistical problems of financial data; relevant to Chapters 7, 8, and 15.

**IV. Market microstructure and transaction costs**

- Larry Harris, *Trading and Exchanges: Market Microstructure for Practitioners*.

Why read: to connect order books, liquidity, spread, market impact, and execution benchmarks into one complete vocabulary; relevant to Chapters 4 and 10.

**V. Position sizing, leverage, and risk budgets**

- The Kelly criterion and works and papers by Edward O. Thorp on its investment applications.
- The sections on position sizing in Van K. Tharp, *Trade Your Way to Financial Freedom*.
- Robert Carver's works on risk targeting, leverage, and portfolio allocation.

Why read: to turn “survive first” into calculable position and portfolio boundaries. Kelly is extremely sensitive to error in estimating an edge; practical research commonly considers fractional Kelly rather than treating the formula as an instruction to go all-in.

**VI. Scientific method and research honesty**

- Karl Popper, *The Logic of Scientific Discovery*.
- Richard Feynman, *Cargo Cult Science*.

Why read: to understand falsifiability, auxiliary assumptions, and research that is formally correct but lacks honest testing; relevant to Chapters 6 and 15.

**VII. Portfolios and expected returns**

- Antti Ilmanen, *Expected Returns*.
- Richard Grinold and Ronald Kahn, *Active Portfolio Management*.

Why read: to learn more about risk exposure, correlation, portfolio construction, and expected returns; relevant to Chapter 12. You will get more from this group after first practicing the data and statistical discipline above.

This appendix ends here. Return to the main text when you need theory, and check each item when you need action. The moment a checklist is most useful is often not when you are at your clearest and calmest, but when you most want to skip it.
