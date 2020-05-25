import tweets as tw
import sentiment as sen


df = tw.get_tweet_df()

new_df = sen.dataframe_sen_pol(df)

print(df)