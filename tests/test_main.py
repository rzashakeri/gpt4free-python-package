import gpt4free
from gpt4free import Provider, forefront

# usage You
response = gpt4free.Completion.create(Provider.You, prompt='Write a poem on Lionel Messi')
print(response)

# usage forefront
token = forefront.Account.create(logging=False)
response = gpt4free.Completion.create(
    Provider.ForeFront, prompt='Write a poem on Lionel Messi', model='gpt-4', token=token
)
print(response)
print(f'END')

# usage theb
response = gpt4free.Completion.create(Provider.Theb, prompt='Write a poem on Lionel Messi')
print(response)
