# The 214-question binary subset

[All 1,005 questions](README.md) · [Binary results](../docs/results.md#errors-on-binary-questions) · [Scoring](../docs/methods.md#binary-error-analysis) · [Download question IDs](../data/binary_subset.csv)

These 214 questions from the 1,005-question set supply the post's precision, recall, false-alarm and missed-detection results. Each has two answer choices and an explicit positive label from its source. Fifteen use adapted choice representations.

Each question page shows its source, reference answer and all 13 recorded model outcomes. Positive choice is the choice key treated as positive in scoring; its meaning varies by source. ‘Correct / answered’ counts saved answers across all 13 models. Questions whose text is obtained separately remain listed with their results and recovery instructions.

## Retrieval · 16 questions

| Question | Source | Positive choice | Correct / answered |
| --- | --- | --- | ---: |
| [is there a new jungle book movie coming out](retrieval/boolq-9fe14fdda69face5bd96.md) | BoolQ | `yes` | 13/13 |
| [do you get paid when on administrative leave](retrieval/boolq-387304ce1c4c16729c75.md) | BoolQ | `yes` | 13/13 |
| [did a helicopter crash in the perfect storm](retrieval/boolq-afa7bbd45dc6974db130.md) | BoolQ | `yes` | 13/13 |
| [can a blighted ovum have a yolk sac](retrieval/boolq-a23fe4476f05d44d34f8.md) | BoolQ | `yes` | 12/13 |
| [was the sears tower ever the tallest building in the world](retrieval/boolq-58a69904d6d6af211123.md) | BoolQ | `yes` | 13/13 |
| [does deadpool have a kid in the comics](retrieval/boolq-ec63ada344a152ccf20a.md) | BoolQ | `yes` | 13/13 |
| [did they film the lord of the rings all at once](retrieval/boolq-bd166e1008ee2e61a4b3.md) | BoolQ | `yes` | 10/13 |
| [roswell do max and liz end up together](retrieval/boolq-748feefbb25d8978aa7e.md) | BoolQ | `yes` | 13/13 |
| [does superman appear in the movie justice league](retrieval/boolq-aff1fc4b8e68bfa8e255.md) | BoolQ | `yes` | 13/13 |
| [is a swift code the same as a bsb number](retrieval/boolq-3c8c7cc30d5666b956b7.md) | BoolQ | `yes` | 12/13 |
| [is a group of cats known as a clowder](retrieval/boolq-23cb00cd216a6370aa39.md) | BoolQ | `yes` | 11/13 |
| [was this the last season of blue bloods](retrieval/boolq-b24921a0b83f87972235.md) | BoolQ | `yes` | 12/13 |
| [is king louie in the jungle book book](retrieval/boolq-5445991716c52c0d47b1.md) | BoolQ | `yes` | 13/13 |
| [did the atlanta falcons get a new stadium](retrieval/boolq-81a93c346c08d802f3e1.md) | BoolQ | `yes` | 13/13 |
| [are the channel islands a part of great britain](retrieval/boolq-1900c9c9ff70e2307a24.md) | BoolQ | `yes` | 13/13 |
| [is there a sequel to batman versus superman](retrieval/boolq-1c12c4b9578fa18abcd1.md) | BoolQ | `yes` | 13/13 |

## Concepts and categorization · 18 questions

| Question | Source | Positive choice | Correct / answered |
| --- | --- | --- | ---: |
| [Does the assistant response refuse the user&#x27;s request?](concepts-and-categorization/wildguardtest-d2654092ac21c03a08a0.md) | WildGuardTest | `refusal` | 13/13 |
| [Recover locally — sentiment](concepts-and-categorization/sst2-0e9044afb18221ffe80e.md) | SST-2 | `1` | 12/13 |
| [Does this user message contain toxic content?](concepts-and-categorization/toxicchat-c2eadd4133a2b1381607.md) | ToxicChat | `1` | 13/13 |
| [Is the user&#x27;s request harmful?](concepts-and-categorization/wildguardtest-25e5223e601a4f4b50c9.md) | WildGuardTest | `harmful` | 13/13 |
| [Recover locally — sentiment](concepts-and-categorization/sst2-0bc47f92d5930466964b.md) | SST-2 | `1` | 13/13 |
| [Does this user message contain toxic content?](concepts-and-categorization/toxicchat-c2b37f09cc23ed460de8.md) | ToxicChat | `1` | 13/13 |
| [Does the assistant response refuse the user&#x27;s request?](concepts-and-categorization/wildguardtest-4652cbf9d2419487a747.md) | WildGuardTest | `refusal` | 13/13 |
| [Recover locally — sentiment](concepts-and-categorization/sst2-5fd857621871033358ce.md) | SST-2 | `1` | 12/13 |
| [Does this user message contain toxic content?](concepts-and-categorization/toxicchat-9fb756a7afa8d0266827.md) | ToxicChat | `1` | 13/13 |
| [Is the user&#x27;s request harmful?](concepts-and-categorization/wildguardtest-2a85c07405e00c9e2101.md) | WildGuardTest | `harmful` | 8/13 |
| [Recover locally — sentiment](concepts-and-categorization/sst2-b0d65a7b0cb8c09e4b43.md) | SST-2 | `1` | 13/13 |
| [Does this user message contain toxic content?](concepts-and-categorization/toxicchat-d11958b049b13a10ae26.md) | ToxicChat | `1` | 13/13 |
| [Does the assistant response refuse the user&#x27;s request?](concepts-and-categorization/wildguardtest-75cda6a766e56c8410f7.md) | WildGuardTest | `refusal` | 13/13 |
| [Recover locally — sentiment](concepts-and-categorization/sst2-57a68c76335ba69b6cfa.md) | SST-2 | `1` | 13/13 |
| [Does this user message contain toxic content?](concepts-and-categorization/toxicchat-aa51edd68d368b1f8cfb.md) | ToxicChat | `1` | 13/13 |
| [Does the assistant response contain harmful content?](concepts-and-categorization/wildguardtest-7a36da6304dbd218c972.md) | WildGuardTest | `harmful` | 10/13 |
| [Recover locally — sentiment](concepts-and-categorization/sst2-e59674342910788e6491.md) | SST-2 | `1` | 13/13 |
| [Does this user message contain toxic content?](concepts-and-categorization/toxicchat-9e7504c4ec24fdaf5061.md) | ToxicChat | `1` | 13/13 |

## Physical cognition · 3 questions

| Question | Source | Positive choice | Correct / answered |
| --- | --- | --- | ---: |
| [Recover locally — boolean](physical-cognition/newton-a190c9a4623ed3ff486b.md) | NEWTON | `1` | 7/13 |
| [Recover locally — boolean](physical-cognition/newton-6c5547eb05c1687b2f10.md) | NEWTON | `1` | 10/13 |
| [Recover locally — boolean](physical-cognition/newton-349743fba2ee777ed23b.md) | NEWTON | `1` | 12/13 |

## Spatial cognition · 15 questions

| Question | Source | Positive choice | Correct / answered |
| --- | --- | --- | ---: |
| [Is the red square above the pink rectangle?](spatial-cognition/babi-ddb5264f42dd626001cb.md) | bAbI | `yes` | 12/13 |
| [Is the triangle above the blue square?](spatial-cognition/babi-f23876e41cd917cc4bba.md) | bAbI | `yes` | 11/13 |
| [Is the yellow square below the triangle?](spatial-cognition/babi-0ba5353f616ba8c27aeb.md) | bAbI | `yes` | 12/13 |
| [Is the pink rectangle below the red square?](spatial-cognition/babi-b44ce789d424787dbc9a.md) | bAbI | `yes` | 12/13 |
| [Is the red square below the yellow square?](spatial-cognition/babi-b50eb35d09f7aceabb8c.md) | bAbI | `yes` | 12/13 |
| [Is the triangle above the blue square?](spatial-cognition/babi-39f6c011fec171169c3c.md) | bAbI | `yes` | 11/13 |
| [Is the triangle to the right of the pink rectangle?](spatial-cognition/babi-9f6e4ed040b09c3c1188.md) | bAbI | `yes` | 11/13 |
| [Is the red square below the red sphere?](spatial-cognition/babi-1633725067b4abc2a83d.md) | bAbI | `yes` | 11/13 |
| [Is the triangle above the red square?](spatial-cognition/babi-68f639273cbeb502d05b.md) | bAbI | `yes` | 11/13 |
| [Is the yellow square to the left of the pink rectangle?](spatial-cognition/babi-453a430bdae501027752.md) | bAbI | `yes` | 11/13 |
| [Is the red sphere above the yellow square?](spatial-cognition/babi-fa5f236b917f8e83ed51.md) | bAbI | `yes` | 10/13 |
| [Is the yellow square below the triangle?](spatial-cognition/babi-d7ab785ce8d485a8f78c.md) | bAbI | `yes` | 11/13 |
| [Is the blue square to the left of the red square?](spatial-cognition/babi-1a78025a4fa9d724a316.md) | bAbI | `yes` | 10/13 |
| [Is the yellow square below the red sphere?](spatial-cognition/babi-237546dc12bd8314dc61.md) | bAbI | `yes` | 12/13 |
| [Is the red square above the red sphere?](spatial-cognition/babi-7552342750ce2b036ff3.md) | bAbI | `yes` | 10/13 |

## Numerical cognition · 15 questions

| Question | Source | Positive choice | Correct / answered |
| --- | --- | --- | ---: |
| [Is smallpox survival less likely than smallpox death overall?](numerical-cognition/cladder-0ff726fd901938516ef1.md) | CLadder | `yes` | 8/13 |
| [Is the chance of black hair larger when observing tanning salon treatment?](numerical-cognition/cladder-59a967d05b9b2ad779d9.md) | CLadder | `yes` | 7/13 |
| [Is glimx more likely than not glimx overall?](numerical-cognition/cladder-20f1de9ceb79fd934b5d.md) | CLadder | `yes` | 11/13 |
| [Is the chance of kwox larger when observing jyka?](numerical-cognition/cladder-74ac992b64fdf90e980b.md) | CLadder | `yes` | 10/13 |
| [Is rukz less likely than not rukz overall?](numerical-cognition/cladder-cec76d739bb7fd0e13a2.md) | CLadder | `yes` | 11/13 |
| [Is rukz less likely than not rukz overall?](numerical-cognition/cladder-f9d0651c0e097afd69b5.md) | CLadder | `yes` | 11/13 |
| [Is muvq more likely than not muvq overall?](numerical-cognition/cladder-6395f9f887de4a2b4365.md) | CLadder | `yes` | 13/13 |
| [Is xevu less likely than not xevu overall?](numerical-cognition/cladder-2ffc9b4a2bdc38318b16.md) | CLadder | `yes` | 8/13 |
| [Is xevu more likely than not xevu overall?](numerical-cognition/cladder-de953b003c3c0272cb76.md) | CLadder | `yes` | 11/13 |
| [Is lirg more likely than not lirg overall?](numerical-cognition/cladder-75588d2e60d3696f8ffd.md) | CLadder | `yes` | 12/13 |
| [Is uvzi less likely than not uvzi overall?](numerical-cognition/cladder-91683d011809ed0714f1.md) | CLadder | `yes` | 9/13 |
| [Is kwox more likely than not kwox overall?](numerical-cognition/cladder-3fe3695ffc0db2f396fc.md) | CLadder | `yes` | 11/13 |
| [Is uvzi less likely than not uvzi overall?](numerical-cognition/cladder-665da985e08fe737ecdd.md) | CLadder | `yes` | 7/13 |
| [Is uvzi more likely than not uvzi overall?](numerical-cognition/cladder-bb3595c6eadc9b7b7a2a.md) | CLadder | `yes` | 9/13 |
| [Is kwox less likely than not kwox overall?](numerical-cognition/cladder-4ac69ecbb53e1c31b43a.md) | CLadder | `yes` | 12/13 |

## Causal reasoning · 57 questions

| Question | Source | Positive choice | Correct / answered |
| --- | --- | --- | ---: |
| [For those who are rixq, would it be less likely to see xevu if the individual was not rixq?](causal-reasoning/cladder-4647c67e29258d071cd6.md) | CLadder | `yes` | 11/13 |
| [To understand how jyka affects kwox, is it more correct to use the Method 1 than Method 2?](causal-reasoning/cladder-9348a489f8c68acc97de.md) | CLadder | `yes` | 9/13 |
| [Will yupt decrease the chance of muvq?](causal-reasoning/cladder-16bfee89bbdefaaa7cae.md) | CLadder | `yes` | 12/13 |
| [If we look at people who are famous, does it mean that attractive appearance affects talent?](causal-reasoning/cladder-9191f10dca8534065205.md) | CLadder | `yes` | 12/13 |
| [If we disregard the mediation effect through swoq, would kwox negatively affect kwoz?](causal-reasoning/cladder-a7a7d38034363c059bd7.md) | CLadder | `yes` | 11/13 |
| [Would an individual is not xevu if not rixq instead of rixq?](causal-reasoning/cladder-de5db69ca3199b264cec.md) | CLadder | `yes` | 9/13 |
| [Does yomx positively affect xevu through gwet?](causal-reasoning/cladder-81555bf547b2ea6266cb.md) | CLadder | `yes` | 11/13 |
| [For those who are jyka, would it be less likely to see lirg if the individual was not jyka?](causal-reasoning/cladder-8bb7bc8217de7fa40d2a.md) | CLadder | `yes` | 11/13 |
| [To understand how jyka affects kwox, is it more correct to use the Method 1 than Method 2?](causal-reasoning/cladder-b9d6be87c28d62330c0c.md) | CLadder | `yes` | 9/13 |
| [If we look at people in a relationship, does it mean that kindness affects attractive appearance?](causal-reasoning/cladder-fed7df3f6e4f44404358.md) | CLadder | `yes` | 12/13 |
| [If we disregard the mediation effect through tijv, would xevo positively affect gyzp?](causal-reasoning/cladder-c268eb68ed9e3d6370eb.md) | CLadder | `yes` | 11/13 |
| [Would Alice arrives at school late if waking up late instead of waking up on time?](causal-reasoning/cladder-c1b53611c57eb17a4fd0.md) | CLadder | `yes` | 11/13 |
| [Does rixq negatively affect xevu through zuph?](causal-reasoning/cladder-dbc6a20f61f6d7d1a64a.md) | CLadder | `yes` | 8/13 |
| [Will kwox decrease the chance of kwoz?](causal-reasoning/cladder-89097ae4c3ec80f08372.md) | CLadder | `yes` | 10/13 |
| [For those who are zuph, would it be less likely to see uvzi if the individual was not zuph?](causal-reasoning/cladder-a1f341b7c52630c0b7a3.md) | CLadder | `yes` | 10/13 |
| [If we look at hospitalized individuals, does it mean that respiratory issues affects broken bones?](causal-reasoning/cladder-4f96ad93a8985d7139d7.md) | CLadder | `yes` | 12/13 |
| [Would an individual is uvzi if zuph instead of not zuph?](causal-reasoning/cladder-38b3bb9d4f17a6fed2bf.md) | CLadder | `yes` | 11/13 |
| [To understand how kwox affects kwoz, is it more correct to use the Method 1 than Method 2?](causal-reasoning/cladder-32768eaa2a51bc76c4e0.md) | CLadder | `yes` | 7/13 |
| [Does pexu negatively affect rukz through hwax?](causal-reasoning/cladder-a90b85ab6575b0fd6603.md) | CLadder | `yes` | 11/13 |
| [Will full moon increase the chance of wet ground?](causal-reasoning/cladder-c28c58d3c5931db96fc6.md) | CLadder | `yes` | 12/13 |
| [If we disregard the mediation effect through wife, would drinking coffee negatively affect alarm clo…](causal-reasoning/cladder-f2c345b705cbb39de70a.md) | CLadder | `yes` | 11/13 |
| [For those who are zuph, would it be more likely to see glimx if the individual was not zuph?](causal-reasoning/cladder-e9579c86d5a53d330206.md) | CLadder | `yes` | 11/13 |
| [If we look at those who are yupt, does it mean that jyka affects kwox?](causal-reasoning/cladder-63ff1f71fe8cd19b9a65.md) | CLadder | `yes` | 12/13 |
| [Would an individual is kwox if not jyka instead of jyka?](causal-reasoning/cladder-07b84e8500950dbc4c33.md) | CLadder | `yes` | 10/13 |
| [Does education level positively affect salary through skill?](causal-reasoning/cladder-d7a13dbb9c03675948a7.md) | CLadder | `yes` | 13/13 |
| [Will jyka decrease the chance of kwox?](causal-reasoning/cladder-2f42ba0ce24a35eaa5b5.md) | CLadder | `yes` | 9/13 |
| [To understand how zuph affects glimx, is it more correct to use the Method 1 than Method 2?](causal-reasoning/cladder-1f081f5f2616e2b22f58.md) | CLadder | `yes` | 8/13 |
| [If we disregard the mediation effect through zuph, would rixq positively affect xevu?](causal-reasoning/cladder-25940bcdf56a887cd372.md) | CLadder | `yes` | 11/13 |
| [For those who are rixq, would it be less likely to see xevu if the individual was not rixq?](causal-reasoning/cladder-4f476d226d4bdf356a4a.md) | CLadder | `yes` | 11/13 |
| [Would the child is intelligent if not liking spicy food instead of liking spicy food?](causal-reasoning/cladder-7f451e24a2bc7cc630bb.md) | CLadder | `yes` | 9/13 |
| [Does smoking positively affect lactose intolerance through effort?](causal-reasoning/cladder-c83f0a0abb5b851bc84e.md) | CLadder | `yes` | 9/13 |
| [If we look at students accepted to elite institutions, does it mean that listening to jazz affects b…](causal-reasoning/cladder-5afc9401ff167a802aa8.md) | CLadder | `yes` | 13/13 |
| [To understand how pexu affects rukz, is it more correct to use the Method 1 than Method 2?](causal-reasoning/cladder-fd74857ae30425cac9c8.md) | CLadder | `yes` | 8/13 |
| [Will xevo decrease the chance of gyzp?](causal-reasoning/cladder-98c63afca5cfbf0762a8.md) | CLadder | `yes` | 11/13 |
| [If we disregard the mediation effect through zupj, would yupt positively affect muvq?](causal-reasoning/cladder-5c7722b390f65fc14dcf.md) | CLadder | `yes` | 11/13 |
| [For those who are xevo, would it be less likely to see gyzp if the individual was not xevo?](causal-reasoning/cladder-02a80ff23d5499cbc69b.md) | CLadder | `yes` | 10/13 |
| [Does pexu negatively affect rukz through hwax and kraz?](causal-reasoning/cladder-c574937d10a7beec03bb.md) | CLadder | `yes` | 12/13 |
| [Would an individual is not lirg if jyka instead of not jyka?](causal-reasoning/cladder-634311372ed0498c91a9.md) | CLadder | `yes` | 13/13 |
| [Will male gender increase the chance of admission acceptance?](causal-reasoning/cladder-b351df72493e1da32fe2.md) | CLadder | `yes` | 12/13 |
| [If we look at those who are gwet, does it mean that yomx affects xevu?](causal-reasoning/cladder-59e8e32297a09f1d6bf7.md) | CLadder | `yes` | 12/13 |
| [To understand how jyka affects kwox, is it more correct to use the Method 1 than Method 2?](causal-reasoning/cladder-7c8838a7e2f0e1432851.md) | CLadder | `yes` | 8/13 |
| [For captains who execute prisoners, would it be less likely to see the prisoner&#x27;s death if the capta…](causal-reasoning/cladder-f4cfa4020dfb290029e1.md) | CLadder | `yes` | 10/13 |
| [Does jyka positively affect kwox through yupt and qwiu?](causal-reasoning/cladder-12c8d26f5c4560a727ba.md) | CLadder | `yes` | 12/13 |
| [Will citrus intake decrease the chance of scurvy?](causal-reasoning/cladder-2f0a7c92e899b91a3926.md) | CLadder | `yes` | 13/13 |
| [Would an individual is uvzi if not zuph instead of zuph?](causal-reasoning/cladder-56d403c69268c1fa5b83.md) | CLadder | `yes` | 11/13 |
| [If we look at hospitalized individuals, does it mean that respiratory issues affects broken bones?](causal-reasoning/cladder-9683b9f6243d51dbea59.md) | CLadder | `yes` | 11/13 |
| [To understand how pexu affects rukz, is it more correct to use the Method 1 than Method 2?](causal-reasoning/cladder-322c2ff202093672e672.md) | CLadder | `yes` | 10/13 |
| [For people who went to tanning salons, would it be more likely to see black hair if the person had n…](causal-reasoning/cladder-589f5cd849b9b83595e4.md) | CLadder | `yes` | 10/13 |
| [Does listening to jazz positively affect lung cancer through tar deposit?](causal-reasoning/cladder-12c7bd5911e08a901a06.md) | CLadder | `yes` | 13/13 |
| [Will encouragement decrease the chance of high exam score?](causal-reasoning/cladder-96489cd386a03a35998f.md) | CLadder | `yes` | 12/13 |
| [Would an individual is not glimx if not zuph instead of zuph?](causal-reasoning/cladder-34f23bd5045077cb4bd7.md) | CLadder | `yes` | 10/13 |
| [If we look at those who are yupt, does it mean that jyka affects kwox?](causal-reasoning/cladder-2e442b0d6902c7d200e7.md) | CLadder | `yes` | 12/13 |
| [For those who are xevo, would it be less likely to see gyzp if the individual was not xevo?](causal-reasoning/cladder-79272deaabce2ac8daa1.md) | CLadder | `yes` | 11/13 |
| [Does pexu positively affect rukz through hwax?](causal-reasoning/cladder-b7409e4c23cce5bcbd65.md) | CLadder | `yes` | 9/13 |
| [Would an individual is muvq if yupt instead of not yupt?](causal-reasoning/cladder-b48bf84e755b59067e3d.md) | CLadder | `yes` | 11/13 |
| [Will tanning salon treatment decrease the chance of tanned skin?](causal-reasoning/cladder-1cb2489995a2e0ea925b.md) | CLadder | `yes` | 12/13 |
| [If we look at those who are zupj, does it mean that yupt affects muvq?](causal-reasoning/cladder-67ee9c9e044e7fae1d97.md) | CLadder | `yes` | 12/13 |

## Uncertainty monitoring · 57 questions

| Question | Source | Positive choice | Correct / answered |
| --- | --- | --- | ---: |
| [If revenge is a dish that’s best served cold, and revenge is sweet, then is revenge ice cream?](uncertainty-monitoring/selfaware-a21b560edfa507c432cb.md) | SelfAware | `no` | 7/13 |
| [do you know the place where the peacock throne is now](uncertainty-monitoring/boolq-2a504c33bb7af95e1320.md) | BoolQ | `yes` | 11/13 |
| [What is a dog&#x27;s responses to stimuli known as?](uncertainty-monitoring/selfaware-34f148904752ec2514a6.md) | SelfAware | `no` | 11/13 |
| [&quot;&quot;&quot;f you wanna make the world a better place, take a look at yourself then make a change&quot;&quot; is a line…](uncertainty-monitoring/selfaware-d2643d86a11227cbc4bd.md) | SelfAware | `no` | 10/13 |
| [On what day of creation did God make the Sun, the Moon and the Stars?](uncertainty-monitoring/selfaware-a154f253a0e5006f796e.md) | SelfAware | `no` | 11/13 |
| [What is the equality of forces between two objects exerting force on each other??](uncertainty-monitoring/selfaware-2b479c2e63b1aad9ecb8.md) | SelfAware | `no` | 13/13 |
| [Conjoined twins are also known as what?](uncertainty-monitoring/selfaware-f3ef02e8bfa8756203ea.md) | SelfAware | `no` | 10/13 |
| [Nancy&#x27;s old washing machine could only wash 9 pieces of clothing at a time. If she had to wash 19 sh…](uncertainty-monitoring/selfaware-439651e6f53ea7a08ec1.md) | SelfAware | `no` | 10/13 |
| [When did the Tertiary period begin?](uncertainty-monitoring/selfaware-952b1221aade40fd330f.md) | SelfAware | `no` | 12/13 |
| [Which primary colour is mixed with white to produce pink?](uncertainty-monitoring/selfaware-cb8fc18f7a8c15850819.md) | SelfAware | `no` | 10/13 |
| [How much money is there in the world?](uncertainty-monitoring/selfaware-7abd95947efcc2b3c8f3.md) | SelfAware | `no` | 8/13 |
| [At 51° 23&#x27; E, what is the easternmost point of the African continent?](uncertainty-monitoring/selfaware-38b07d3302a5fd5b77db.md) | SelfAware | `no` | 11/13 |
| [Where do all of those who have died go after they die?](uncertainty-monitoring/selfaware-7fa389f5af37ab9bf485.md) | SelfAware | `no` | 12/13 |
| [For radio broadcast that one would hear in their car what type of towers are used?](uncertainty-monitoring/selfaware-4377e96fd257a74ae1c6.md) | SelfAware | `no` | 10/13 |
| [The diet of what mythical monster periodically included seven youths and seven maidens?](uncertainty-monitoring/selfaware-093386d3996f6db19b7d.md) | SelfAware | `no` | 11/13 |
| [&quot;Billy Blaze, an 8-year-old genius who constructed a spaceship in his backyard from old soup cans an…](uncertainty-monitoring/selfaware-29334c1ca9df70f176dd.md) | SelfAware | `no` | 9/13 |
| [What restaurant chain with over 15,000 locations is a sister franchise to Wing Street?](uncertainty-monitoring/selfaware-a84fd3aac838986e9bc9.md) | SelfAware | `no` | 10/13 |
| [What substance are feathers, fingernails and hair made of?](uncertainty-monitoring/selfaware-a4e126e4bb0c7700e623.md) | SelfAware | `no` | 11/13 |
| [Which monthly magazine is based on food entertainment, Club or Food Network Magazine?](uncertainty-monitoring/selfaware-cd2df85dd338d447d206.md) | SelfAware | `no` | 11/13 |
| [What are teeth made out of?](uncertainty-monitoring/selfaware-70500a0d24fc6a21b47b.md) | SelfAware | `no` | 11/13 |
| [Besides the moon, what is the brightest object in the night sky?](uncertainty-monitoring/selfaware-18f3ec901e666d4ded28.md) | SelfAware | `no` | 13/13 |
| [What is karma and how does it operate within us during different lifetimes?](uncertainty-monitoring/selfaware-2dcfb3405c6e561b3444.md) | SelfAware | `no` | 6/13 |
| [Who did Sirhan Sirhan assassinate?](uncertainty-monitoring/selfaware-1056df989172e9ed7837.md) | SelfAware | `no` | 12/13 |
| [Carol and her mom were picking carrots from their garden. Carol picked 29 and her mother picked 16. …](uncertainty-monitoring/selfaware-48c2f213861e852409bd.md) | SelfAware | `no` | 9/13 |
| [Are adolescents or children better able to understand that people do not have complete control over …](uncertainty-monitoring/selfaware-bf6ed17c2652fa9ceea8.md) | SelfAware | `no` | 10/13 |
| [If we knew what created the bing bang, do you think we would try to do it again?](uncertainty-monitoring/selfaware-ca4b066815da2c17a8a4.md) | SelfAware | `no` | 12/13 |
| [Which country has the highest nominal wealth per adult in the world according to Credit Suisse?](uncertainty-monitoring/selfaware-8d0d95394030c2c3831f.md) | SelfAware | `no` | 13/13 |
| [In deism is God represented in human form?](uncertainty-monitoring/selfaware-8bd3ecb78014e52f1154.md) | SelfAware | `no` | 10/13 |
| [Who was right about reincarnation: Was Buddha right about reincarnation and Hindus were wrong, or vi…](uncertainty-monitoring/selfaware-d1385bd9f54fe4bc29c5.md) | SelfAware | `no` | 11/13 |
| [When we forget, where does the information go?](uncertainty-monitoring/selfaware-f6bfb7ec4fee0708fd16.md) | SelfAware | `no` | 11/13 |
| [What is known as artificial light that is excessive or intrusive?](uncertainty-monitoring/selfaware-712c5869a2e6b457f778.md) | SelfAware | `no` | 10/13 |
| [Do you think a singularity will happen in this century?](uncertainty-monitoring/selfaware-ba57e74868f86e08800b.md) | SelfAware | `no` | 11/13 |
| [What is our place in an infinite universe?](uncertainty-monitoring/selfaware-81b2aa615ecf0da6fe47.md) | SelfAware | `no` | 12/13 |
| [Are lies better than harsh truths?](uncertainty-monitoring/selfaware-f9665a6cacb1d6482ba7.md) | SelfAware | `no` | 11/13 |
| [What incident killed Diana in Paris?](uncertainty-monitoring/selfaware-be1c4b47b233aca0d4fd.md) | SelfAware | `no` | 9/13 |
| [Is a turtle homeless or naked, without a shell?](uncertainty-monitoring/selfaware-d0b92e0feeaef0f0a481.md) | SelfAware | `no` | 6/13 |
| [Would time continue if everything in the world was frozen?](uncertainty-monitoring/selfaware-21758758c6c5557765de.md) | SelfAware | `no` | 9/13 |
| [Stonehenge is in which UK county?](uncertainty-monitoring/selfaware-9dacdba1f3708265dcb1.md) | SelfAware | `no` | 10/13 |
| [Where does the lost time go to?](uncertainty-monitoring/selfaware-b867ed1afee9e6f877eb.md) | SelfAware | `no` | 11/13 |
| [What is the nautical term for a staircase between two decks on a ship?](uncertainty-monitoring/selfaware-4e9a25ff5abb43e03479.md) | SelfAware | `no` | 11/13 |
| [If data scientists had the ability to accurately predict who was more likely to commit crimes in the…](uncertainty-monitoring/selfaware-c5d8f12c844a482c0417.md) | SelfAware | `no` | 10/13 |
| [In the Bible who was the son of Abraham and Sarah?](uncertainty-monitoring/selfaware-0df7918430d916f376ea.md) | SelfAware | `no` | 11/13 |
| [Will the advancement of today’s technologies yield a net positive or a net negative result?](uncertainty-monitoring/selfaware-3d4e212e2207b6fcb865.md) | SelfAware | `no` | 11/13 |
| [What type of sleep involves dreaming?](uncertainty-monitoring/selfaware-270c1f0db417ff876172.md) | SelfAware | `no` | 10/13 |
| [Walter Pauk created the note-taking system devised in what decade?](uncertainty-monitoring/selfaware-2617b181ac78b7fca77a.md) | SelfAware | `no` | 10/13 |
| [Which large fleshy fruit of the far east has been banned from some public areas because of it&#x27;s dist…](uncertainty-monitoring/selfaware-b3e1cb1d590c96b8b5e3.md) | SelfAware | `no` | 12/13 |
| [How many strings are there on a Viola?](uncertainty-monitoring/selfaware-92f42aa8af31e0bac639.md) | SelfAware | `no` | 11/13 |
| [Would you rather have to wear a bib every time you go out to eat or drink from a sippy cup every tim…](uncertainty-monitoring/selfaware-78e32e9988edd5bb8db5.md) | SelfAware | `no` | 10/13 |
| [If you were a nyctophobic, what would you fear?](uncertainty-monitoring/selfaware-d5cf1390460dc58293e3.md) | SelfAware | `no` | 11/13 |
| [How long will people remember you after you die?](uncertainty-monitoring/selfaware-960edd90fa887df08317.md) | SelfAware | `no` | 11/13 |
| [What eight letter word do americans use to call what we British call a dressing gown?](uncertainty-monitoring/selfaware-f510e282c58e179e19df.md) | SelfAware | `no` | 12/13 |
| [Is the Higgs-Boson machine a good or bad thing for our universe?](uncertainty-monitoring/selfaware-c330451f2e56e240dd9c.md) | SelfAware | `no` | 10/13 |
| [Who is a senior servant in a large household, specifically in charge of the dining room, wine cellar…](uncertainty-monitoring/selfaware-fe379b6f9694b997b9dd.md) | SelfAware | `no` | 11/13 |
| [Who invented the art of milking a cow?](uncertainty-monitoring/selfaware-20b980f26cd1c889217a.md) | SelfAware | `no` | 11/13 |
| [How do vampires dress so fancy if they can’t see their reflections?](uncertainty-monitoring/selfaware-fc8794c056e241d0024b.md) | SelfAware | `no` | 11/13 |
| [How many undiscovered animals are there in the world?](uncertainty-monitoring/selfaware-c9befb66ce11310c1323.md) | SelfAware | `no` | 11/13 |
| [In Australia, on which side of the road do motorists drive?](uncertainty-monitoring/selfaware-eb0490cc160fcd752726.md) | SelfAware | `no` | 10/13 |

## Communication · 29 questions

| Question | Source | Positive choice | Correct / answered |
| --- | --- | --- | ---: |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-50039007b81a935b1eb9.md) | iSarcasmEval | `yes` | 9/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-e98c5b028eaa58641346.md) | iSarcasmEval | `yes` | 10/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-45c45bec9b1cd8bdf58c.md) | iSarcasmEval | `yes` | 13/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-9bdecb6b9c2d39051c5c.md) | iSarcasmEval | `yes` | 6/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-426ae11bba4946c001b4.md) | iSarcasmEval | `yes` | 13/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-84e132ca8ad34e36e699.md) | iSarcasmEval | `yes` | 8/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-a1521ecf9b0e44a2bc78.md) | iSarcasmEval | `yes` | 8/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-f1b6f854c28c919983af.md) | iSarcasmEval | `yes` | 12/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-04ddce5a258223b7721c.md) | iSarcasmEval | `yes` | 12/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-6012a8260570a330f0af.md) | iSarcasmEval | `yes` | 13/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-d3d91247737226bc30f5.md) | iSarcasmEval | `yes` | 11/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-0c701168ab2dcae3fb24.md) | iSarcasmEval | `yes` | 13/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-b0e229556fd68b33ae7d.md) | iSarcasmEval | `yes` | 11/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-49d205abacd16b1589b6.md) | iSarcasmEval | `yes` | 13/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-cb3b0623041aa5e4b431.md) | iSarcasmEval | `yes` | 13/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-696c52736e472e33f11e.md) | iSarcasmEval | `yes` | 8/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-d12cb55491be9199d70a.md) | iSarcasmEval | `yes` | 13/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-045b4295d9bb572acadc.md) | iSarcasmEval | `yes` | 9/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-3abe6ec5adac85690586.md) | iSarcasmEval | `yes` | 7/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-4ec1a4e2bb26bca00738.md) | iSarcasmEval | `yes` | 9/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-ce36d80b31f48cb352a7.md) | iSarcasmEval | `yes` | 13/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-5182c292c492b5b9162f.md) | iSarcasmEval | `yes` | 13/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-bfcf69cad7b345fb8301.md) | iSarcasmEval | `yes` | 13/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-275fe91b6129debd4fb6.md) | iSarcasmEval | `yes` | 8/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-35f5cfae72759e9cdfbd.md) | iSarcasmEval | `yes` | 13/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-6805cca11e8ee9bf3dcc.md) | iSarcasmEval | `yes` | 12/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-015bc09c82beb2679504.md) | iSarcasmEval | `yes` | 10/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-b94d363d6aa7bca77b93.md) | iSarcasmEval | `yes` | 13/13 |
| [Is this message intended to be sarcastic?](communication/isarcasmeval-8ba18d128291212e9332.md) | iSarcasmEval | `yes` | 13/13 |

## Rule application · 4 questions

| Question | Source | Positive choice | Correct / answered |
| --- | --- | --- | ---: |
| [Does the target assistant step contain an error under a process-quality evaluation? A correct useful…](rule-application/agentprocessbench-7c762735ad5a6506cb30.md) | AgentProcessBench | `yes` | 12/13 |
| [Does the target assistant step contain an error under a process-quality evaluation? A correct useful…](rule-application/agentprocessbench-b9cc901195f5efcde072.md) | AgentProcessBench | `yes` | 11/13 |
| [Does the target assistant step contain an error under a process-quality evaluation? A correct useful…](rule-application/agentprocessbench-ec7638061fdfb29b7061.md) | AgentProcessBench | `yes` | 9/13 |
| [Does the target assistant step contain an error under a process-quality evaluation? A correct useful…](rule-application/agentprocessbench-6f0f18ee83772088ae6a.md) | AgentProcessBench | `yes` | 11/13 |
