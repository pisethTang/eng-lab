# Description (verbatim from meetup page)

When Lambda launched in 2014 the rules were simple: Node.js only, stateless, one request at a time, 60 seconds and done. More languages followed and the limit reached 15 minutes in 2018, but the rest held for over a decade.

In the last twelve months AWS has rewritten them.

"A Lambda function" now means one of five things:

Event Functions: classic Lambda, renamed in October. Your code doesn't change.
Web Functions: an ordinary web server, with one environment serving many requests at once and no CPU billed while it waits.
Durable Functions: checkpointed workflows that can wait for a human and pick up where they left off, up to a year later.
MicroVMs: isolated sandboxes for running AI-generated code, which suspend and resume with memory and disk intact.
Managed Instances: Lambda on EC2 in your own account.
Most of this is aimed at AI agents, which spend their time waiting on a model, run for hours, and run code nobody has reviewed.

Is Lambda still "serverless"? And does it matter?

Rick Morgans will walk through each of the five using BLACK FRIDAY, a hypothetical multiplayer game in which every team inherits the same online shop and has to get it through the holiday rush, balancing customer retention, reliability and cost. The most profitable shop wins.

Each kind of Lambda has a job in the game. Web Functions run the arena, and Durable Functions run each round, pausing for the organiser between stages. Event Functions judge every team's shop in parallel, and MicroVMs give each team's untrusted code its own sandbox. Managed Instances could take over the judging once there's enough steady work to keep a pool busy.



# Link to event 

https://www.meetup.com/amazon-web-services-user-group-adelaide/events/317283526/?eventOrigin=home_page_upcoming_events%24all