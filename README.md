# F1-Data-Analysis

![image](https://github.com/user-attachments/assets/3c90f600-2c35-46d0-95e2-685920b72386)

## Introduction 
Formula 1 (F1) is an elite motorsport that produces a wealth of data, encompassing everything from car telemetry to driver statistics and race outcomes. This project leverages advanced data analysis techniques to extract valuable insights from F1 data, with the goal of enhancing team performance, refining race strategies, and improving overall results.
This repository showcases a comprehensive analysis of Formula One data, current up to the 2023 Bahrain Grand Prix. The analysis is conducted using Python, employing libraries such as Pandas, NumPy, and Matplotlib to process and visualize the data effectively.
By diving deep into this rich dataset, I aim to uncover patterns, trends, and correlations that can provide a competitive edge in the high-stakes world of Formula 1 racing. This project offers a fascinating exploration of how data science can be applied to one of the world's most technologically advanced sports.

## Data Source
This analysis utilises a comprehensive Formula 1 dataset sourced from Kaggle, a platform for data science projects and competitions. The dataset encompasses a wealth of information on F1 drivers, including details about their career spans, race performances, and championship points accumulated. It provides a rich resource for exploring various aspects of Formula 1 racing history and driver statistics.

## Data Cleansing 
In preparing the dataset for analysis, I encountered various challenges with data quality and consistency. To address these issues, I implemented a comprehensive data cleaning process using the Pandas library.
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

Key Competiive Insights:
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
Correlation Between Number of Seasons and Race Wins:
The **correlation coefficient** between the number of seasons a driver participates in (Years_Active) and their number of race wins (Race_Wins) is **0.504**. This moderate positive correlation suggests that, generally, drivers who participate in more seasons tend to win more races. However, it's not a perfect correlation, indicating that while there's a trend, other factors also influence race wins.

Model Performance:
The **Mean Squared Error** of the RandomForestRegressor model is **22.31**. MSE is a measure of the average squared difference between predicted and actual values. A lower MSE indicates better model performance. In this case, the MSE value indicates that the model’s predictions have some deviation from the actual race wins, but the exact degree of error is context-dependent.

Key Competitive Inisights:
- Moderate Correlation: The moderate correlation coefficient implies that increasing the number of seasons a driver competes in is associated with an increase in race wins, though not perfectly. Teams should consider both the experience gained from additional seasons and other variables that may affect race performance.

- Model Accuracy: The RandomForestRegressor model's MSE suggests that while the model provides some insight, there is room for improvement in predicting race wins based on the number of seasons. Other factors and more sophisticated modeling techniques might yield better predictions.

Strategic Implications:
- Talent Development: The positive correlation highlights the value of retaining experienced drivers who have accumulated more seasons. Teams might invest in nurturing their drivers over longer periods to increase their chances of achieving more race wins.

- Data Enrichment: Given the MSE, it’s advisable to incorporate additional features into the model to improve its predictive power. Factors such as driver skill level, team support, and race conditions could enhance prediction accuracy.

- Performance Monitoring: Regularly monitoring and updating the model with new data can help teams better understand the evolving relationship between experience and performance, leading to more strategic decisions about driver management and race strategies.

### 3 - For drivers who have achieved champion status, what is the relationship between their podium finishes and pole positions?

![Linear_Regression](https://github.com/user-attachments/assets/019c65b3-ea14-466a-9f1a-9a11d6816732)

Staistical overview:
Prediction Score: 68.34%
Correlation Coefficient: 0.93
R-squared (R²): 0.86

Key Competiive Insights:
- Pole position as a Critical Success Factor
For drivers who have achieved champion status, securing pole position is highly advantageous. The strong correlation (0.93) and high R-squared value (0.86) suggest that drivers starting at the front of the grid are much more likely to finish in the top three. Teams and drivers that consistently secure pole positions are more likely to be successful and win races, given their strong correlation with podium finishes.

- Qualifying Performance is Crucial
The ability to perform well in qualifying sessions is essential for achieving high race results. Pole positions provide a significant advantage that translates into higher podium finishes. Focusing on improving qualifying performance can lead to better race outcomes, as starting from the front significantly enhances the chances of finishing in the top positions.

Strategic Implications:
- Investment in Qualifying Speed
Investing in technologies and innovations that improve qualifying performance, such as advanced aerodynamics, optimized setups, and tire strategies tailored for qualifying. By enhancing their qualifying speed, teams can secure more pole positions, thereby increasing their chances of winning races and improving their overall standings in the championship.

- Focus on Pole Position Strategies
Develop specific strategies for qualifying sessions that focus on achieving the best possible starting positions. This might include fine-tuning car setups for short, high-pressure runs, and optimizing driver performance in qualifying conditions. Teams that master these strategies will have a better chance of securing pole positions and, therefore, will likely see a higher rate of podium finishes and race wins.

- Race Strategy Alignment
Align race strategies with the advantages of starting from pole position. For instance, plan for optimal tire management and pit stop strategies that capitalize on the advantage of starting at the front. Effective alignment of race strategies with pole position advantages ensures that teams can maintain their front-row position throughout the race, maximizing their chances of podium finishes.


### 4 - What factors contribute significantly to a driver becoming a champion?

## Conclusion 

## Refrences 
Kaggle dataset: https://www.kaggle.com/datasets/dubradave/formula-1-drivers-dataset
