setwd('C:/Users/Eric/Desktop/rymbot')
reviews <- read.csv(file.path("home_crawl.csv"), sep=",")
reviews <- unique(reviews[c("album", "artist", "year", "genre", "ratings", "ranking", "rating", "reviews")])

reviews$album[reviews$album==""] <- "NA"
reviews$year[reviews$year==""] <- "NA"
reviews$year[reviews$year=="year"] <- "NA"
reviews$ratings[reviews$ratings==""] <- "NA"

reviews$ratings <- as.numeric(as.character(reviews$ratings))
reviews$rating <- as.numeric(as.character(reviews$rating))
reviews$reviews <- as.numeric(as.character(reviews$reviews))
reviews$ranking <- as.numeric(as.character(reviews$ranking))

reviews.clean <- na.omit(reviews)

summary(reviews.clean)
class(reviews.clean$ratings)

aggregate(reviews.clean$rating~reviews.clean$year, FUN=mean)
aggregate(reviews.clean$ratings~reviews.clean$year, FUN=sum)