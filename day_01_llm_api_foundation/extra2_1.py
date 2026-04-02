from solution.solution import call_openai

for temp in [0.0, 0.5, 1.0, 1.5]:
    response, latency = call_openai('Hãy kể cho tôi một sự thật thú vị về Việt Nam.', temperature=temp)
    print(f'\n--- Temperature {temp} (latency: {latency:.2f}s) ---')
    print(response)
