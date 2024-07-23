# F1-Data-Analysis

![image](https://github.com/user-attachments/assets/3c90f600-2c35-46d0-95e2-685920b72386)

## Introduction 
Formula 1 (F1) is an elite motorsport that produces a wealth of data, encompassing everything from car telemetry to driver statistics and race outcomes. This project leverages advanced data analysis techniques to extract valuable insights from F1 data, enhance team performance, refine race strategies, and improve overall results.
This repository showcases a comprehensive analysis of Formula One data, current up to the 2023 Bahrain Grand Prix. The study uses Python, employing libraries such as Pandas, NumPy, and Matplotlib to process and visualize the data effectively.
By diving deep into this rich dataset, I aim to uncover patterns, trends, and correlations that can provide a competitive edge in the high-stakes world of Formula 1 racing. This project offers a fascinating exploration of how data science can be applied to one of the world's most technologically advanced sports.

## Data Source
This analysis utilises a comprehensive Formula 1 dataset sourced from Kaggle, a platform for data science projects and competitions. The dataset encompasses a wealth of information on F1 drivers, including details about their career spans, race performances, and championship points accumulated. It provides a rich resource for exploring various aspects of Formula 1 racing history and driver statistics.

## Data Cleansing 
In preparing the dataset for analysis, I encountered various challenges with data quality and consistency. To address these issues, I implemented a comprehensive data-cleaning process using the Pandas library.
Initially, I examined the dataset for missing values and inconsistencies in data types. Using Pandas, I methodically removed or imputed missing values as appropriate, and converted data types to ensure they were suitable for my intended analyses.

## Data Analysis 
I conducted a thorough analysis of the data to uncover insights and address several key questions pertaining to Formula 1 racing. My approach incorporated correlation analysis and data visualisation, utilising the Matplotlib library.

In this study, I explored the following questions:

- How are driver nationalities distributed within this dataset?
- To what extent does the number of seasons a driver competes correlate with their race win tally?
- For drivers who have achieved champion status, what is the relationship between their podium finishes and pole positions?
- What factors contribute significantly to a driver becoming a champion?

My analysis employed various statistical techniques and graphical representations to elucidate patterns and relationships within the data, providing a comprehensive view of Formula 1 driver performance and success factors.

### 1 - How are driver nationalities distributed within this dataset?

![PieChart](https://github.com/user-attachments/assets/c3c9dbb5-7161-4a81-8b05-9a00ad163b58)

The analysis of driver nationalities in Formula 1 reveals a diverse yet unevenly distributed representation across various countries. This distribution provides insights into the global reach and historical development of the sport.

Key Competitive Insights:
- Dominant Talent Pools:
The United Kingdom (20.4%) and United States (19.9%) emerge as the primary sources of F1 drivers. Teams focusing recruitment efforts in these countries may have access to a larger, more experienced talent pool.

- Established European Networks:
The strong representation from European countries (UK, Italy, France, Germany, etc.) suggests well-developed motorsport infrastructures. Teams could leverage these existing networks for driver development programs and technical partnerships.

- Emerging Markets:
Countries with growing representation (e.g., Brazil, Japan, Australia) present opportunities for market expansion, fan engagement, and potentially untapped talent sources. Investing in these regions could yield long-term competitive advantages.

- Diversity as a Strength:
The presence of at least 20 nationalities indicates a global talent spread. Teams embracing diversity might gain unique perspectives on racing strategies and car development, potentially leading to innovative approaches.

- Historical Strongholds vs. New Entrants:
Traditional F1 nations (e.g., UK, Italy) contrast with newer entrants (e.g., Japan, Finland). This dynamic offers opportunities for blending established expertise with fresh approaches to racing.

- Targeted Development Programs:
Countries with lower representation but strong motorsport cultures (e.g., Netherlands, Belgium) could be prime targets for focused driver development initiatives, potentially yielding high-quality talent with less competition.

- Global Appeal for Sponsorships:
The international distribution of drivers opens avenues for diverse sponsorship opportunities, allowing teams to tap into various national markets for financial and technical partnerships.

Strategic Implications:

- Diversified Recruitment: This approach ensures access to both established talent pools and potentially undiscovered prodigies. By scouting talent from emerging markets as well as traditional powerhouses, teams can tap into a broader range of skills and perspectives, which can be crucial for gaining a competitive edge.

- Localised Development Centres: Establishing training facilities in key regions (such as the UK, Italy, and France) provides easier access to local talent and existing motorsport infrastructure. This can streamline talent development and improve team performance by leveraging local expertise and resources.

- Cross-Industry Partnerships: Collaborations with automotive and technology firms in countries with strong F1 presence can lead to innovative technical solutions and knowledge transfer. These partnerships can drive technological advancements and improve the team's overall performance on track.

- Targeted Fan Engagement: Tailoring marketing efforts to align with driver nationalities can significantly boost fan engagement in specific countries, enhancing viewership and merchandise sales. This can help build a stronger global fan base and increase the team's commercial success.

- Driver Development Programmes: Implementing programmes in underrepresented countries with strong motorsport cultures can uncover unique talent and build a pipeline of future stars. This long-term investment ensures sustained team performance and helps in developing a loyal fan base.

### 2 - To what extent does the number of seasons a driver competes correlate with their race win tally?
Correlation Between the Number of Seasons and Race Wins:
The **correlation coefficient** between the number of seasons a driver participates in (Years_Active) and their number of race wins (Race_Wins) is **0.504**. This moderate positive correlation suggests that, generally, drivers who participate in more seasons tend to win more races. However, it's not a perfect correlation, indicating that while there's a trend, other factors also influence race wins.

Model Performance:
The **Mean Squared Error** of the RandomForestRegressor model is **22.31**. MSE is a measure of the average squared difference between predicted and actual values. A lower MSE indicates better model performance. In this case, the MSE value indicates that the model’s predictions have some deviation from the actual race wins, but the exact degree of error is context-dependent.

Key Competitive Insights:
- Moderate Correlation: The moderate correlation coefficient implies that increasing the number of seasons a driver competes in is associated with an increase in race wins, though not perfectly. Teams should consider both the experience gained from additional seasons and other variables that may affect race performance.

- Model Accuracy: The RandomForestRegressor model's MSE suggests that while the model provides some insight, there is room for improvement in predicting race wins based on the number of seasons. Other factors and more sophisticated modelling techniques might yield better predictions.

Strategic Implications:
- Talent Development: The positive correlation highlights the value of retaining experienced drivers who have accumulated more seasons. Teams might invest in nurturing their drivers over longer periods to increase their chances of achieving more race wins.

- Data Enrichment: Given the MSE, it’s advisable to incorporate additional features into the model to improve its predictive power. Factors such as driver skill level, team support, and race conditions could enhance prediction accuracy.

- Performance Monitoring: Regularly monitoring and updating the model with new data can help teams better understand the evolving relationship between experience and performance, leading to more strategic decisions about driver management and race strategies.

### 3 - For drivers who have achieved champion status, what is the relationship between their podium finishes and pole positions?

![Linear_Regression](https://github.com/user-attachments/assets/019c65b3-ea14-466a-9f1a-9a11d6816732)

Statistical overview:
Prediction Score: 68.34%
Correlation Coefficient: 0.93
R-squared (R²): 0.86

Key Competitive Insights:
- Pole position as a Critical Success Factor
For drivers who have achieved champion status, securing pole position is highly advantageous. The strong correlation (0.93) and high R-squared value (0.86) suggest that drivers starting at the front of the grid are much more likely to finish in the top three. Teams and drivers that consistently secure pole positions are more likely to be successful and win races, given their strong correlation with podium finishes.

- Qualifying Performance is Crucial
The ability to perform well in qualifying sessions is essential for achieving high race results. Pole positions provide a significant advantage that translates into higher podium finishes. Focusing on improving qualifying performance can lead to better race outcomes, as starting from the front significantly enhances the chances of finishing in the top positions.

Strategic Implications:
- Investment in Qualifying Speed
Investing in technologies and innovations that improve qualifying performance, such as advanced aerodynamics, optimized setups, and tyre strategies tailored for qualifying. By enhancing their qualifying speed, teams can secure more pole positions, thereby increasing their chances of winning races and improving their overall standings in the championship.

- Focus on Pole Position Strategies
Develop specific strategies for qualifying sessions that focus on achieving the best possible starting positions. This might include fine-tuning car setups for short, high-pressure runs, and optimizing driver performance in qualifying conditions. Teams that master these strategies will have a better chance of securing pole positions and, therefore, will likely see a higher rate of podium finishes and race wins.

- Race Strategy Alignment
Align race strategies with the advantages of starting from pole position. For instance, plan for optimal tyre management and pit stop strategies that capitalize on the advantage of starting at the front. Effective alignment of race strategies with pole position advantages ensures that teams can maintain their front-row position throughout the race, maximizing their chances of podium finishes.


### 4 - What factors contribute significantly to a driver becoming a champion?
![Correlation_Matrix](https://github.com/user-attachments/assets/5252a83e-a604-49f0-b9a3-9e6684835274)
Key Competitive Insights:
- Race Wins: Unsurprisingly, race wins have the strongest correlation (0.92) with championships. This means that drivers who consistently win races are more likely to become champions.

- Pole Positions: There is also a very strong correlation (0.87) between pole positions and championships. Securing the pole position gives the driver a significant advantage in terms of starting the race first and avoiding potential accidents at the start.

- Podiums: Finishing on the podium consistently (0.81) is another important factor.

- Points: Scoring points regularly (0.66) is vital for accumulating points throughout the season.

Strategic Implications:
- Develop Race-Winning Skills: The data suggests that the most important factor is developing the skills and strategies necessary to win races consistently. This could involve focusing on car control, racecraft, overtaking skills, and wet weather driving.

- Qualify Well: Qualifying towards the front of the grid is crucial for race wins and championship contention. Focus on car setup and one lap pace to achieve this.

- Maintain Consistent Performance: Even if you are not winning every race, it is important to finish on the podium and score points consistently. This means avoiding mistakes and crashes and managing the car effectively throughout the race.

Additional Insights:
- Experience: There is a moderate correlation (0.42) between years active and championships. This suggests that experience is somewhat beneficial, but not the most important factor.

- Race Starts: Interestingly, there is a weak negative correlation (-0.75) between race starts and championships. This may be because drivers who participate in more races throughout their careers may not be focusing on winning championships in every season.

![Linear](https://github.com/user-attachments/assets/793c15d1-6208-4e34-9d7d-80d2649013f6)
Key Competitive Insights:
- Win Rate vs. Pole Rate: There is a positive correlation between win rate and pole rate, which means that drivers who start the race in first place tend to win more races. This aligns with the findings from the heatmap.

- Start Rate vs. Podium Rate: There appears to be a positive correlation between a driver's starting position and their podium finish rate. Drivers who start closer to the front have a better chance of finishing on the podium.

Strategic Implications:
- Qualifying is Important: Securing a good starting position through qualifying is crucial for race wins and podium finishes.

- Early Race Strategy: Since drivers who start in front tend to finish there, race strategy should focus on maintaining the lead or overtaking those ahead in the early laps.

![HeatMapRed](https://github.com/user-attachments/assets/bde51cfe-8026-4f86-ba3a-df6a1ba9775f)
Based on the provided information and the high accuracy **(0.988)** and precision **(0.994)** achieved by the model, we can glean the following key competitive insights:
- Importance of Race Performance Metrics: The chosen features (Race_Entries, Race_Starts, Pole_Positions, Race_Wins, Podiums, Fastest_Laps, Points) all relate directly to a driver's performance on the track. This suggests that a driver's historical performance in these areas is a strong indicator of their future championship potential.

- Focus on Consistency and Top Performances: The model appears to weigh both consistency metrics (Race Entries, Race Starts, Points) and top performance metrics (Pole Positions, Race Wins, Podiums, Fastest Laps) heavily. This indicates that not only winning races but also consistently performing well throughout the season is crucial for becoming a champion.

Strategic Implications:
- Develop All-Around Skills:  Focus on honing both race-winning skills (overtaking, racecraft) and maintaining consistent performance throughout the season (car management, avoiding mistakes).

- Prioritize Qualifying and Race Starts:  Securing good starting positions through strong qualifying performances is critical as it improves the chances of winning races and finishing on the podium.

- Maintain Consistency:  Don't just focus on winning every race.  Finishing consistently in the points and avoiding mistakes is equally important for accumulating points and championship contention.
<p align="center">
  <img src="https://github.com/user-attachments/assets/dd3b0bf4-28d2-4af8-b63b-1c9a2d12a4fe" alt="HeatMapBlue">
</p>


True Positives (TP): 1 - This represents the number of drivers who were correctly predicted to become champions (actually became champions).
False Negatives (FN): 0 - This represents the number of drivers who were incorrectly predicted not to become champions (actually became champions - missed by the model).
False Positives (FP): 0 - This represents the number of drivers who were incorrectly predicted to become champions (did not actually become champions).
True Negatives (TN): 0.71 - This represents the number of drivers who were correctly predicted not to become champions (did not actually become champions).

The normalize='true' argument normalizes the confusion matrix by dividing each cell by the total number of test samples (number of drivers in the test set). This provides a percentage representation of how often each prediction category occurred.

Key Competitive Insights:
- No False Positives (FP): There are zero drivers predicted to be champions who did not actually become champions (FP = 0). This is ideal as it indicates the model avoids falsely identifying non-champions as potential champions.

- Missed Champions (FN): There are a small number of drivers (0.29) who were champions but the model predicted they wouldn't be (FN). This represents the model's limitation in identifying some potential champions.

Strategic Improvements:
- Focus on Identifying Future Champions (Reduce FN): Investigate the characteristics of the drivers the model missed (FN) to understand potential limitations and areas for improvement. This might involve incorporating additional features or refining the model architecture.


## Conclusion 
The comprehensive analysis of Formula 1 data has provided valuable insights into several key areas of driver and team performance. By leveraging advanced data analysis techniques, we have identified significant patterns and correlations that can inform strategies to enhance team performance, refine race strategies, and improve overall results.

Enhancing Team Performance analysis highlights the critical importance of securing pole positions for achieving podium finishes, emphasising the need for strong qualifying performance. Technology and strategies that improve qualifying performance, such as advanced aerodynamics and optimised setups should be implemented to increase the likelihood of securing pole positions and achieving better race results.

Refining Race Strategies insights from the data indicate the necessity of aligning race strategies with qualifying outcomes and maintaining consistent performance throughout the season. Focuses should be made on pole position strategies developed strategies should be specified for qualifying sessions to secure the best starting positions, thereby increasing the chances of race wins. In addition to consistent performance, emphasis should be made on the importance of consistent race finishes and avoiding mistakes to accumulate points steadily.

By implementing these strategic insights, teams can enhance their competitive edge, improve race outcomes, and achieve sustained success in the high-stakes world of Formula 1 racing.

## Limitations
- Data quality and consistency can impact analysis.
- Unforeseen circumstances in races can influence outcomes even if models predict otherwise.
- Machine learning models, while powerful, are not perfect and require ongoing refinement.

## Refrences 
Kaggle dataset: https://www.kaggle.com/datasets/dubradave/formula-1-drivers-dataset
