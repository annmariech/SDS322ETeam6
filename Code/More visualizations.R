data <- read.csv("~/crashdata.csv")
fatal <- read.csv("~/dataset_merged.csv")
library(tidyr)
library(dplyr)

# CREATING VARIABLES
## for the total number of people hurt in accident (injury or death)
data1 <- data %>% mutate(number_hurt = (tot_injry_cnt + death_cnt))
## for the hour
data2 <- data1 %>% separate("crash_time", c("Hour", "Minute", "Second"))

# GRAPHS
## number of crashes by hour
data2 %>% group_by(Hour) %>% summarize(crash_hour = n_distinct(crash_id)) %>% ggplot(aes(x = Hour, y = crash_hour)) + geom_col(fill = "black") + xlab("Hour")+ ylab("Number of Crashes") + ggtitle("Number of Crashes by Hour") + theme(panel.background = element_blank(), panel.border = element_rect(colour = "black", fill=NA, size=.5))
## number hurt (injuries + deaths) by hour, have to get rid of NAs in number_hurt var
data2 %>% group_by(Hour) %>% summarize(hurt_by_hour = sum(number_hurt, na.rm=TRUE)) %>% ggplot(aes(x = Hour, y = hurt_by_hour)) + geom_col() + xlab("Hour")+ ylab("Number Hurt (Injured + Dead)") + ggtitle("Number Hurt in All Collisions over Hour of Day")
## number of fatalities by hour
data2 %>% group_by(Hour) %>% ggplot(aes(x = Hour, y = death_cnt)) + geom_col() + xlab("Hour")+ ylab("Number of Fatalities") + ggtitle("Number of Fatalities in All Collisions over Hour of Day") + theme_minimal()


## ran red light
fatal %>% filter(ran_red_light == "y" | ran_red_light == "n") %>% ggplot(aes(x=hour, y=number_of_fatalities, fill = ran_red_light)) + geom_col() + xlab("Hour") + ylab("Number of Fatalities") + ggtitle("Fatalities by Hour and Ran Red Light") + theme_minimal()