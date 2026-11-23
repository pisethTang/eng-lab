# adelaide.js October 2026 Meetup

- **Date:** Thursday 22 October 2026, 5:30 to 7:30 PM
- **Venue:** KWP+Partners, Level 1/251 Rundle St, Adelaide
- **Sponsors:** Encode Talent, KWP+Partners, Qantas
- **Organisers:** Darragh Kearns, Brett Earle, Simon Cook

---

## Before the event: prep

You're in for tonight, 5:30 to 7:30 PM at KWP+Partners, Level 1/251 Rundle St. About 62 people are going.

### What the talks will likely cover

#### Talk 1: TypeScript without losing your sanity

*Torbs van Heeswijck, Engineering Manager at Splose*

TypeScript is JavaScript with types added. The compiler checks your code for errors before it runs. Likely topics:

- **Strict mode:** compiler settings that catch more bugs.
- **Avoiding `any`:** `any` turns off type checking, so overusing it defeats the purpose.
- **Narrowing and discriminated unions:** ways to make TypeScript work out exactly which shape of data you're holding.
- **Legacy vs greenfield:** adding TypeScript to an old codebase gradually, compared with starting a new project strict from day one.
- **Coaching angle:** since he's a manager, expect material on getting a team to adopt good TypeScript habits.

#### Talk 2: DOMinoes

*James Armitage, Developer at KWP+Partners*

- **DOM** is the browser's live structure of the page.
- **Virtual DOM** is a copy kept in memory (React uses one). The framework compares the old and new copies, then updates only what changed.

The trend he'll probably cover is frameworks dropping the virtual DOM:

- **Signals / fine-grained reactivity:** each value knows exactly which part of the page depends on it and updates that part directly. Used in Solid, Svelte 5 "runes", Angular signals and Vue "Vapor mode".
- **Compilers:** the framework does work at build time so less runs in the browser. Examples: Svelte and the React Compiler.
- **Performance trade-offs:** speed, bundle size, and developer experience.

### How to network

- **Arrive at 5:30.** The 20 minutes before the welcome are the easiest time to talk. People are standing around with nothing to do yet.
- **Use the talks as openers.** "Do you use strict mode at work?" or "Have you tried signals yet?" are easy questions anyone in the room can answer.
- **Talk to the speakers afterwards.** Ask one specific question about their talk. That's more memorable than "great talk."
- **Know the sponsors:**
  - **Encode Talent:** a tech recruiter. Useful if you're job hunting.
  - **KWP+Partners:** the host venue and a digital agency. James works there.
  - **Qantas:** they're hiring (their careers page is listed as the sponsor link).
- **Organisers:** Darragh Kearns, Brett Earle, Simon Cook. Say hi and thank them. They know everyone and the event prioritises regulars, so being known by them helps you get in next time.
- **Follow up within 24 hours.** Connect on LinkedIn and mention one thing you talked about.

### How to position yourself

- **Have a 10-second intro ready:** who you are + what you work on + what you're looking for.

  > Example: "I'm Seth, I build [X] with [React/TypeScript]. I'm keen to [find a frontend role / learn from people shipping at scale / find collaborators]."

- **Be specific.** "I'm learning frontend" is forgettable. "I'm building a booking app in Next.js and fighting TypeScript errors" starts a conversation.
- **Ask more than you talk.** People remember who was interested in them.
- **Have your LinkedIn or GitHub QR code ready** on your phone.

What's your main goal tonight: finding a job, learning, or meeting collaborators? I can tighten your intro around that.

### Your intro

> "Hi, I'm Seth. I'm a grad-level frontend developer, mostly React and Next.js, and I've also worked with Vue. I'm looking for my first full-time frontend role in Adelaide."

If they ask what you've built, have one project ready in a single sentence: what it does, the stack, and one hard problem you solved.

### Your edge: you know React and Vue

Most juniors only know React. Knowing two frameworks means you can compare them, and that is exactly what James's talk is about. Use it.

### Questions for Torbs (TypeScript talk)

- "For a junior joining a legacy codebase, what TypeScript habit would you want them to have from day one?"
- "When you coach juniors, what TypeScript mistake do you see most?"
- **Follow-up:** "Does Splose take on grads or juniors?"

He's a manager, so these show him you're thinking about how you'd fit into a team.

### Questions for James (DOMinoes talk)

- "I've used React and Vue. Is Vue's Vapor mode worth learning now, or is it too early?" (We defined Vapor mode in my first reply: Vue without the virtual DOM.)
- "Does React's move to a compiler make signals less important for React devs?" (Signals and the React Compiler were also defined in my first reply.)
- **Follow-up:** "What does KWP mostly build with?" This works well because KWP is an agency, and agencies often use multiple frameworks.

### Questions for Encode Talent

- "What are Adelaide companies looking for in junior frontend devs right now?"
- "Is React plus Next.js enough, or should I add something like testing or backend skills?"
- "Can I send you my CV after tonight?"

### Mindset

- At grad level, people hire for curiosity and attitude, not deep experience. Asking good questions shows both.
- Don't apologise for being junior. Say what you're learning next, for example "I'm getting deeper into TypeScript strict mode right now." Tonight's talk gives you that line.

Good luck tonight.

---

## After the event: notes and takeaways

> **Source notes:** these are taken from my photos of the slides and an auto-generated audio transcript. The transcript is noisy, so anything marked [unclear] is my best reading and should be double-checked.

### 1. Talk: "DOMinoes": what falls when you remove the virtual DOM?

**Speaker:** James Armitage, Developer at KWP+Partners

#### Key ideas

##### What the DOM and virtual DOM are

- **DOM (Document Object Model):** the browser's live representation of everything on the page. Code changes the page through it.
- **Virtual DOM:** a second copy of the page kept in memory by frameworks like React and Vue. When state changes, a diffing algorithm compares old and new copies, then updates only what changed. This process is called **reconciliation**.

##### The tally stick story (his opening)

- Medieval England recorded debts on notched wooden sticks, split in two. Each party kept a half. Matching the halves later proved the record. Two copies, reconciled.
- Used for about 700 years. When they were retired, the stockpile was burned all at once, overheated the furnace, and burned down the Palace of Westminster (1834).
- **Point:** the virtual DOM also keeps two copies and reconciles them. It was a brilliant solution for its time (2013).

##### Costs of the virtual DOM

- Needs a runtime that knows how to diff.
- Keeps a second copy of the DOM in memory.
- Diffing work grows with component size.

**Benefits:** small compiled components and a simple mental model ("re-render, and the diff does the heavy lifting").

##### The alternative: direct DOM updates

- Smarter compilers plus signals (values that know exactly which parts of the page depend on them) allow updating the DOM directly with no second copy.
- The compiler works out at build time which DOM nodes connect to which piece of state. When state changes, only that node updates.
- **Frameworks doing this:** Svelte (pioneer), Solid, and now Vue Vapor (release candidate).
- **Drawbacks:** each component carries its own wiring code, and the dependency graph uses memory.
- **Benefits:** tiny runtime, very precise updates.
- Angular sits somewhere in between; he left it aside.

##### Why Vue Vapor matters

- Vue Vapor is Vue rewritten to do direct DOM updates.
- You can mix virtual-DOM components and Vapor components in one app, or go fully Vapor.
- Switching a component takes one change: add `vapor` to the script tag, e.g. `<script setup vapor>`.
- This allows a fair comparison for the first time: same codebase, same framework, only the rendering strategy changes. Previous comparisons were across different frameworks, so other differences got mixed in.

##### His benchmark

Self-built test app: a big table, create/update/swap/remove rows, run ~1,000 times.

**Download size (Vue vs Vue Vapor):** barely changes, at most about 3 KB difference. Vapor's size grows with the number of components, since each carries its own wiring.

**Time to respond to a click** (from slide):

| Action        | Vue     | Vue Vapor                   |
| ------------- | ------- | --------------------------- |
| Select a row  | 6.0 ms  | 0.9 ms                      |
| Update rows   | 26.7 ms | 19.8 ms                     |
| Swap two rows | 42.0 ms | 35.7 ms                     |
| Remove a row  | 52.5 ms | ~4x.6 ms (cut off in photo) |

His take: faster, but in milliseconds most users will not notice.

**Memory with 10,000 rows** (from slide):

| Framework | Memory  | Approach               |
| --------- | ------- | ---------------------- |
| Svelte    | 12.5 MB | No virtual DOM         |
| Vue Vapor | 13.3 MB | No virtual DOM         |
| Solid     | 13.3 MB | No virtual DOM         |
| Angular   | 14.1 MB | Angular (own approach) |
| React     | 19.9 MB | Virtual DOM            |
| Vue       | 21.8 MB | Virtual DOM            |
| Preact    | 22.6 MB | Virtual DOM            |

This is the clear win: Vue Vapor uses about 40% less memory than standard Vue. Keeping the virtual DOM in memory has a real cost.

**Time for the page to become interactive:** results varied more. Some virtual-DOM frameworks were comparable to direct-DOM ones, so here the framework itself mattered more than the virtual DOM [unclear which frameworks were the outliers].

##### His conclusions

- Removing the virtual DOM gives a clear memory saving and some speed gain. The rest depends on the framework.
- The bigger difference is how you think:
  - **React:** "redraw everything, let the diff work out what changed."
  - **Signal-based frameworks:** "these values are live on the page and update themselves."
- Benchmarks cannot measure ecosystem, libraries, or your team. That is where frameworks like Angular shine.
- **Closing line from the tally sticks:** retiring them was right, burning them all in one day was the mistake. The virtual DOM is still the right answer for many teams. If your constraints have changed, experiment. Vue Vapor lets you migrate one component at a time.

#### Q&A highlights

- **Why did frameworks use a virtual DOM in the first place?** Before it, apps updated the DOM manually (jQuery style), which was clunky. React's virtual DOM was a revolution at the time.
- **When would you pick a direct-DOM framework?** Consider inertia: rewriting an existing React SPA is expensive. Example: he built a small widget embedded in a WordPress site, where loading a small fast framework made more sense than loading React.
- **What about server-side rendering?** A separate problem that optimises for a different thing (first page load). Not covered by this comparison.

### 2. Talk: "How to write TypeScript without losing your sanity"

**Speaker:** Torbjorn (Torbs) van Heeswijck, Engineering Manager at Splose (payments team)

#### What goes wrong

- **Strict mode is off, or partly off.** Turning it on in a migrated JavaScript codebase gives a huge number of errors.
- **Casts everywhere**, especially `as unknown as X`, which he calls "go away, TypeScript."
- **Overly broad function parameters.** Example: a function that prints a delivery label takes the whole `Order`, but only needs an ID, name and recipient. Result: every test has to cast mock data to satisfy fields it does not use.
- **Impossibly vague types.** Slide example: a `Customer` interface with about 80 fields, 58 of them optional. With n optional fields there are 2ⁿ combinations, so this type allows 37 quintillion possible shapes. It means nothing.
- **Types that lie:** fields marked optional that are never missing, or marked always-present when they can be null.

**Result:** the codebase expects every developer to know everything, because the types do not tell them.

#### The AI angle

- AI agents copy your patterns and believe your types.
- He has seen agents spend thousands of tokens tracing a request path to check whether a value can be undefined. In one case the database typed money as a decimal when it is always a whole number.
- Someone still has to review the code.

#### What to do instead

##### Understand the fundamentals *(slide)*

- **Types disappear at run time.** TypeScript only checks at compile time.

  ```ts
  interface Dog { name: string; age: number }
  const fido = JSON.parse('{ "name": "Fido" }') as Dog;
  fido.age.toFixed(); // TypeError at run time
  ```

- **Shapes matter, names don't** (structural typing). Any object with the right fields fits the type.

  ```ts
  const theory = { name: "Catalysis", age: 232, by: "Fulhame" };
  const dog: Dog = theory; // compiles
  ```

- **Types are sets.** A type is the set of values it allows. Narrowing shrinks the set.

  ```ts
  const first = items[0];          // string | number | undefined
  if (typeof first === 'string') {
    first.toUpperCase();           // string
    items[0].toUpperCase();        // ERROR
  }
  ```

##### Make things easy for the compiler *(slide)*

- **Make the compiler strict:**

  ```json
  "strict": true,
  "noUncheckedIndexedAccess": true
  ```

  He thinks not doing this is "a really bad idea."

- **Parse data at the edge.** Data entering your program should start as `unknown`, then be checked immediately. Do not tell a function "trust me, I know what this is."

  ```ts
  const OrderQuerySchema = z.object({
    status: z.enum(['pending', 'shipped', 'delivered']),
    from: z.coerce.date(),
    to: z.coerce.date(),
  });
  const query = OrderQuerySchema.parse(req.query);
  ```

- **Keep types specific.** A function should ask only for what it uses.

##### Let the compiler infer types *(slide)*

- **Construct, don't mutate.** Build new values from small steps. TypeScript tracks these well; it struggles with objects that are created and then changed over time.

  ```ts
  const details = prepareDetails(request);
  const name = capitalise(details.name);
  const person = { ...details, name };
  ```

- **Write as little TypeScript as you can.** If most of your code needs explicit type annotations, something is wrong. The compiler does most of the work.

TypeScript "wants to be an immutable functional language" but has to support how people write JavaScript.

##### Use generics sparingly *(slide)*

- Use a generic when two types need to change together, e.g. keep the input's extra fields in the output:

  ```ts
  function capitaliseName(person: { name: string }): { name: string }
  capitaliseName(person).id;   // ERROR

  function capitaliseName<T extends { name: string }>(person: T): T
  capitaliseName(person).id;   // number
  ```

- **Avoid single-use generic parameters.** If `T` appears only once, it is just a normal parameter.
- `axios.get<Organisation>(...)` is just a cast in disguise. Nothing checks the response.
- TypeScript's type system is powerful enough to run Doom. "Please resist that."

##### What good code looks like *(slide)*

A request schema in Zod, a narrow `OrderStore` type, and a handler that takes `body: unknown`, parses it, then lets the compiler know every type from there on. Once you are there, he rarely needs to run code to trust it.

#### How to get there in a legacy codebase

##### There is no single switch *(slide)*

- **One flag, one package at a time.** Small package: turn on full strict. Big package: start with `noImplicitAny`. Split code into packages if needed (the strangler pattern: gradually replace an old system piece by piece).
- **Flip it now, suppress what breaks.** Add `// @ts-expect-error` above each error. Once fixed, TypeScript reports the directive as unused, so you know to delete it.
  - **Warning:** he has seen a production bug where `@ts-expect-error` in a test hid a different error.
- The null/undefined checks are about 80% of the errors.

##### Make the types honest first *(slide)*

If the database allows `NULL`, the type should say so:

```ts
middleName: string;          // before
middleName: string | null;   // the database allows NULL
```

Even if you revert it because it causes 800 errors, you learned something.

##### Freeze it, then shrink it *(slide)*

Turn a lint rule (e.g. `@typescript-eslint/no-unsafe-call`) on as an error everywhere, with a `legacyExceptions` file list that only ever gets shorter.

##### Start at the edges *(slide)*

Parse request bodies, partner API responses, and `catch (err: unknown)`.

Key question: **"Where does unknown data enter your program?"**

**His biggest learning:** fixing a wrong type deep inside the codebase cascades. Fix one error, get five more, then 200.

#### Q&A highlights

- **What if the whole thing is JavaScript with no clear boundaries?** Write an adapter layer and gradually break the code into packages. Converting a large JS codebase in one go probably will not work, because JavaScript tends to be written very differently (giant objects rebuilt all the time). At some point you are effectively rewriting.
- **The hard part is product risk.** Making a type honest can mean "we now throw if this is ever null," which may break something a customer relies on. That needs product and support involved, plus release flags. Estimate the work, then double or triple it.
- **Instructions for AI agents (`CLAUDE.md`, `AGENTS.md` etc.):**
  - He cited research where most extra instructions made agents worse at writing tests than no instructions, because they caused useless extra work.
  - **What seems to work:** small, focused guidance files (e.g. a testing guide with "techniques to use" and "traps to avoid"). Then ask the agent, in a fresh context, to review its work against that file.
  - **Docs rule:** never let the agent write JSDoc comments about the current ticket or conversation ("we did this to avoid the sheet problem"). The next reader has no context.
  - AI rarely asks how to design types (generic or two separate types?). He suspects it was trained on a lot of poor types.
- **Alternatives to Zod?** His favourite library has nicer syntax, but the team would need to learn it. He is increasingly leaning towards writing validation yourself: LLMs can generate the boilerplate, it is easy to read, and pulling in untrusted dependencies is becoming riskier (supply chain attacks). Zod does integrate well with things like Express decorators.
- **Why he's not a React fan:** React is good for small apps. At large scale, contexts and hooks drift from its original idea: put data in, get the same UI out every time.
- **When is TypeScript not worth it?** Small team, or a system you can hold in your head. Its main value: working in another team's code safely, types as documentation, and onboarding people who have never seen the code.

#### Resources (from his final slide)

| Resource                                  | Link                                                                 |
| ----------------------------------------- | -------------------------------------------------------------------- |
| The strict flag                           | <https://www.typescriptlang.org/tsconfig/#strict>                    |
| Zod                                       | <https://zod.dev>                                                    |
| Handbook: Generics                        | <https://www.typescriptlang.org/docs/handbook/2/generics.html>       |
| Handbook: Creating types from types       | <https://www.typescriptlang.org/docs/handbook/2/types-from-types.html> |
| Making sense of TypeScript using set theory | <https://thoughtspile.github.io/2023/01/23/typescript-sets>        |
| typescript-eslint no-unsafe-call          | <https://typescript-eslint.io/rules/no-unsafe-call>                  |
| Type challenges                           | <https://github.com/type-challenges/type-challenges>                 |

**His tip:** do the first 15 to 20 type challenges. They are useless in production, but they teach how generics really work.

### 3. Pub conversation with Erick (Forestree), The Elephant

#### About Forestree

- A small startup (about 5 to 6 people). Erick has been there about 2 to 2.5 years.
- **Product:** a tree asset management platform for councils. Councils manage tens of thousands of trees (he mentioned 60,000 to 80,000 for one city) and carry liability if a branch falls and injures someone.
- **Features:** map every tree (species, age, diameter, disease), raise and track jobs with risk levels (high/low), inspections, assign contractors who log work in the platform, scheduled maintenance like watering.
- **GPS feature:** when a contractor's truck stays near a tree for a set time, the work is logged automatically, since drivers should not be touching phones.
- Works closely with customers; feature requests get quoted by estimated dev, testing and feedback time.
- **Tech:** uses Vue at work. [unclear: backend possibly Node.js and C#/.NET]

#### Why he prefers Vue over React

He built a side project (an education platform for teachers) first in Next.js, then after 1 to 2 months rewrote it in Vue + Nuxt. Using Vue at work and React at night let him compare directly.

- **React is great for an MVP, harder after.** "MVP with React is amazing, but after MVP" it became tiring to maintain.
- **Lifecycle hooks vs `useEffect`.** Vue has specific hooks (`onMounted`, `onBeforeMount` etc.). React folds most of this into `useEffect`, which gets hard to control when several effects update each other.
- **React guidance keeps changing.** Example: "don't use Context, use a store," then newer guidance says Context is fine for simple data. Also "you should never use `useEffect`." He finds Vue more stable.
- **Templates are easier to read.** Conditionals in JSX use ternaries, which add nesting and indentation. Vue's directives (`v-if`, `v-else`) keep it flat. He disliked directives at first (they reminded him of Angular's `ngIf`) but now prefers them.
- **Composables organise logic well.** You can group state, functions and computed values for one feature together, then move them into a separate composable file. Easier to read than one large component.
- **Two-way binding is optional.** Vue offers `v-model` (two-way binding), or you can wire it manually for more granular control. React only has the manual way.

#### Why Nuxt over Next (for his project)

- His product is login-only and sold directly to teachers (the owner visits schools and demos it). So SEO is irrelevant, and blazing-fast first render is not the priority.
- What matters: consistency and reliability.
- He mainly renders client-side, but Nuxt lets him choose per route whether to render on the client or server. He keeps server rendering as an option for heavy pages, e.g. loading large amounts of data that would strain the browser's memory.

**Product philosophy he shared:** "a product for everyone that can do anything is not for anyone." Build features for all customers, not one-off variations.

### Other things from the evening

- **Opening slide from the organisers:** be nice, supportive and open; don't stand in closed circles, let people in; ask the stupid question you want to ask.
- **Sign-up survey:** React was the most popular favourite framework, Vue second.
- **Qantas Product Innovation Centre** (sponsor pitch):
  - New team building Qantas's customer-facing digital products, including [Qantas.com](http://Qantas.com) (their largest e-commerce platform).
  - Hiring some of their first front-end teams. New office on Currie Street.
  - "AI-native" way of working, using GitHub Copilot. Recent internal hackathon project is being taken to production.
  - Described as feeling like a startup inside Qantas. Contact them via the careers page.
- **DDD Adelaide:** community tech conference next month, $60 including food and coffee, limited tickets.
- adelaide.js is moving from Meetup to Luma for future events.
- **Other pub chats** [speakers unclear in transcript]:
  - A startup building a car-service history platform (Next.js for speed, planning to move to Express or Hono later).
  - A hospitality startup that tried AI voice agents for restaurant orders. Voice worked for bookings but struggled with similar-sounding menu items, so they switched to a standard click-to-order flow.
  - **Lesson shared:** a new way of doing something has to be 10x better before people change habits.

### 4. My takeaways

- **Vue Vapor is the one to watch.** For the first time you can compare virtual DOM vs direct DOM updates inside one framework, and migrate one component at a time. The memory saving (~40%) is real; the speed gain is small.
- The framework debate is shifting from "virtual DOM or not" to "how do you want to think about state."
- **TypeScript: trust the compiler, and make it trustworthy.** Turn on `strict` and `noUncheckedIndexedAccess`, parse unknown data at the edges, keep types narrow and honest, and let inference do the work.
- **In legacy code, migrate gradually:** one flag or package at a time, freeze the problems, then shrink the list.
- **Good types help AI too.** Agents believe your types, so wrong types waste time and tokens.

### 5. Ideas to build on

- **Extend James's benchmark:** add the React Compiler, Svelte 5 and Angular signals to the same table test, and publish the results.
- **A Vue to Vue Vapor migration demo:** convert one component at a time and measure memory at each step.
- **A TypeScript "strictness ratchet" template:** a small repo showing `@ts-expect-error`, a shrinking `legacyExceptions` list, and Zod parsing at the edges.
- **Type challenges:** work through the first 20 and write up what each taught me.

### 6. Contacts to follow up

- [ ] Erick (Forestree): LinkedIn, mention the Vue vs React chat
- [ ] Torbs van Heeswijck (Splose): thank him, ask a follow-up about migrating legacy code
- [ ] James Armitage (KWP+Partners): ask about his benchmark repo
- [ ] Qantas Product Innovation Centre: check front-end roles
- [ ] Encode Talent: send CV

### Glossary

| Term                          | Meaning                                                                                                                             |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Compile time / run time       | Compile time is when TypeScript checks and converts your code; run time is when the code actually executes in the browser or server. |
| Signals                       | Reactive values that track exactly which parts of the UI depend on them and update only those parts.                               |
| Structural typing             | TypeScript decides if a value fits a type by its shape (fields), not by its name.                                                   |
| Narrowing                     | TypeScript working out a more specific type from checks like `typeof x === 'string'`.                                               |
| Generic                       | A type that takes another type as input, e.g. `Array<string>`.                                                                      |
| Zod                           | A library that checks data at run time and produces matching TypeScript types.                                                      |
| Strangler pattern             | Replacing an old system gradually, piece by piece, while it keeps running.                                                          |
| Composable (Vue)              | A function that groups related state and logic so it can be reused or moved out of a component.                                     |
| SSR (server-side rendering)   | Generating the page's HTML on the server, mainly to speed up first load and help SEO.                                               |

---

## Reference
