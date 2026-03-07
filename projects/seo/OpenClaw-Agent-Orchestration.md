# OpenClaw Agent Orchestration Research

**Comprehensive guide for building and orchestrating subagents in OpenClaw**

*Compiled: March 2026*

---

## Part 1: Agent Spawning

### sessions_spawn Tool Parameters

#### Core Parameters

**task** (Required, String)
- The task/prompt for the subagent to complete
- Full description of what needs to be done
- Can include context, requirements, expected output
- Example: "Research the latest SEO trends for 2025 and compile a comprehensive report"

**label** (Optional, String)
- Human-readable name for the subagent
- Used in `/subagents list` and `/subagents info`
- Helps identify specific subagent runs
- Example: "SEO Research 2025", "Content Audit", "Keyword Research"

**agentId** (Optional, String)
- Spawn subagent under a different agent's identity
- Default: Spawns under same agent as requester
- Requires allowlist configuration
- Use case: Access different tools or auth profiles

**model** (Optional, String)
- Override model for this specific subagent run
- Format: `provider/model` (e.g., `anthropic/claude-sonnet-4`)
- Invalid values are skipped with warning
- Precedence: explicit model > agents.defaults.subagents.model > requester's model

**thinking** (Optional, String)
- Override thinking level for subagent
- Levels: `off`, `minimal`, `low`, `medium`, `high`, `xhigh`
- GPT-5.2 + Codex models support thinking
- Precedence: explicit thinking > agents.defaults.subagents.thinking > requester's thinking

**runTimeoutSeconds** (Optional, Integer)
- Abort subagent run after N seconds
- Default: `agents.defaults.subagents.runTimeoutSeconds` when set, otherwise `0` (no timeout)
- Does NOT auto-archive; only stops the run
- Use case: Prevent runaway subagents

**thread** (Optional, Boolean, Default: false)
- Request channel thread binding for this subagent session
- Only supported on Discord currently
- When true, creates or binds a thread to the session
- Follow-up messages in thread route to same subagent session

**mode** (Optional, String: `"run"` | `"session"`)
- Default: `"run"`
- If `thread: true` and `mode` omitted, default becomes `"session"`
- **mode: "run"**: One-shot execution, announces result back to requester
- **mode: "session"**: Requires `thread: true`, creates persistent session

**cleanup** (Optional, String: `"delete"` | `"keep"`)
- Default: `"keep"`
- **cleanup: "delete"**: Archives immediately after announce (keeps transcript via rename)
- **cleanup: "keep"**: Subagent remains until auto-archive

#### Runtime Options

**Runtime: "subagent"** (Default)
- Runs as subagent session
- Session key: `agent:<agentId>:subagent:<uuid>`
- Announces result back to requester chat
- Isolated from main session context
- Tool policy: All tools except session tools (unless configured)

**Runtime: "acp"** (ACP Harness)
- Runs in external ACP harness (Codex, Claude Code, Gemini CLI)
- Requires `runtime: "acp"` in sessions_spawn
- Used for specific IDE/integration workflows
- Different tool surface and capabilities

#### Session Persistence

**One-shot vs Persistent Sessions**

**One-shot (mode: "run")**:
- Executes task once
- Announces result back to requester
- Session remains but doesn't respond to follow-up
- Default behavior for subagents

**Persistent (mode: "session" + thread: true)**:
- Creates long-running session bound to Discord thread
- Follow-up messages in thread route to same session
- Use `/unfocus` to detach manually
- Auto-unfocus after TTL (configurable)
- Best for: Ongoing conversations, iterative work

**Auto-Archive Behavior**:
- Subagent sessions auto-archived after `agents.defaults.subagents.archiveAfterMinutes`
- Default: 60 minutes
- Archive uses `sessions.delete` with transcript rename to `*.deleted.<timestamp>`
- Pending timers lost on gateway restart
- Applies equally to depth-1 and depth-2 sessions

### Model Selection for Subagents

#### Default Model Hierarchy

1. **Explicit model in sessions_spawn** (Highest priority)
2. **agents.defaults.subagents.model** (Config override)
3. **Requester's model** (Inherited from parent session)

#### Configuration Examples

**Set default subagent model**:
```json5
{
  agents: {
    defaults: {
      subagents: {
        model: "google-gemini/gemini-2-flash"
      }
    }
  }
}
```

**Per-agent subagent model**:
```json5
{
  agents: {
    list: [
      {
        id: "seo-writer",
        subagents: {
          model: "anthropic/claude-3-haiku"
        }
      }
    ]
  }
}
```

**Override at spawn time**:
```
sessions_spawn({
  task: "Research SEO trends",
  model: "google-gemini/gemini-2-flash"  // Override
})
```

#### Cost Optimization Strategy

**Use cheaper models for subagents**:
- Main agent: High-quality model (Claude Sonnet, GPT-4)
- Subagents: Fast/cheap models (Gemini Flash, Haiku, FlashX)
- Research tasks: FlashX (fast data gathering)
- Analysis tasks: Haiku (quick summarization)
- Writing tasks: Sonnet (quality content)

**Why**: Each subagent has its own context and token usage
- Main agent on expensive model = strategic planning, complex decisions
- Subagents on cheap models = scalable parallel work
- Example: 10 subagents × Gemini Flash ($0.0001/1K) = much cheaper than 10 × Claude Sonnet ($0.015/1K)

#### Thinking Level Override

**Default thinking hierarchy**:
1. **Explicit thinking in sessions_spawn** (Highest)
2. **agents.defaults.subagents.thinking** (Config)
3. **Requester's thinking** (Inherited)

**Configuration**:
```json5
{
  agents: {
    defaults: {
      subagents: {
        thinking: "minimal"  // Reduce token usage
      }
    }
  }
}
```

**Use cases**:
- `off`: Simple data fetching, no chain-of-thought needed
- `minimal`: Quick decisions, straightforward tasks
- `low`: Analysis with some reasoning
- `medium`: Complex planning, multi-step workflows
- `high`/`xhigh`: Only for GPT-5.2/Codex, deep reasoning

---

## Part 2: Agent Management

### subagents Tool

#### List Subagents

**Action**: `list`

**What it shows**:
- All subagent runs for current requester session
- Run ID, label, status, timestamps
- Session key, session ID, transcript path
- Runtime/token stats (for completed runs)

**Usage**:
```
/subagents list
subagents({ action: "list" })
```

**Output format**:
```
ID | Label | Status | Created | Runtime | Tokens
---|-------|--------|---------|---------|-------
#1 | SEO Research | running | 2m ago | - | -
#2 | Content Audit | completed | 15m ago | 5m12s | 12,345
```

#### Kill Subagent

**Action**: `kill <id|#|all>`

**Parameters**:
- `<id>`: Specific run ID or label to kill
- `<#>`: Reference by list number
- `all`: Kill all subagents for requester session

**Cascade Behavior**:
- Stops specified subagent
- Cascades to all its children (nested subagents)
- Announces back with status: "killed"

**Usage**:
```
/subagents kill #1
/subagents kill SEO Research
/subagents kill all
subagents({ action: "kill", target: "#1" })
```

#### View Subagent Log

**Action**: `log <id|#> [limit] [tools]`

**Parameters**:
- `<id|#>`: Run ID or list number
- `[limit]`: Number of lines to show (default: all)
- `[tools]`: Show only tool calls/results

**Use cases**:
- Debug subagent execution
- Check what tools it used
- Review progress without reading full transcript

**Usage**:
```
/subagents log #1 50
/subagents log SEO Research tools
subagents({ action: "log", sessionId: "..." })
```

#### Get Subagent Info

**Action**: `info <id|#>`

**What it shows**:
- Full run metadata
- Status, timestamps, session key
- Transcript path
- Model, thinking level
- Tool policy (what tools available)
- Cleanup status

**Usage**:
```
/subagents info #1
/subagents info SEO Research
subagents({ action: "info", sessionId: "..." })
```

#### Send Message to Subagent

**Action**: `send <id|#> <message>`

**What it does**:
- Injects message into running subagent's queue
- Subagent receives message next turn
- Only works for running subagents

**Use cases**:
- Steering ongoing work
- Providing additional context
- Correcting direction mid-task

**Usage**:
```
/subagents send #1 Focus on voice search, not technical SEO
subagents({ action: "send", sessionId: "...", data: "New instructions..." })
```

#### Steer Subagent

**Action**: `steer <id|#> <message>`

**Same as send**: Alias for inject message into subagent's queue

**Usage**:
```
/subagents steer #1 Narrow scope to local SEO only
subagents({ action: "steer", sessionId: "...", message: "..." })
```

#### Spawn Subagent (Manual)

**Action**: `spawn <agentId> <task> [--model <model>] [--thinking <level>]`

**Parameters**:
- `<agentId>`: Agent to spawn under (default: current agent)
- `<task>`: Task description
- `--model`: Override model
- `--thinking`: Override thinking level

**Difference from sessions_spawn**:
- `/subagents spawn` is a user command, not internal tool call
- Sends final completion update back to requester when run finishes
- Non-blocking: Returns run ID immediately
- One-shot mode (mode: "run")

**Usage**:
```
/subagents spawn seo-writer Research 2025 SEO trends
/subagents spawn my-agent Write a blog post about keyword research --model gemini-flash
```

### Monitoring Long-Running Subagents

#### Status Monitoring

**Check status periodically**:
```
/subagents list  // See all runs and statuses
/subagents info #1  // Get detailed status
/subagents log #1  // Check progress
```

#### Common Statuses

**running**: Subagent is actively working
**completed**: Subagent finished successfully
**failed**: Subagent encountered error
**timed out**: Hit runTimeoutSeconds limit
**killed**: Manually stopped via kill command

#### Timeout Configuration

**Set default timeout**:
```json5
{
  agents: {
    defaults: {
      subagents: {
        runTimeoutSeconds: 900  // 15 minutes default
      }
    }
  }
}
```

**Per-subagent timeout**:
```
sessions_spawn({
  task: "...",
  runTimeoutSeconds: 1800  // 30 minutes for this run only
})
```

**Important**: Timeout does NOT auto-archive; session remains until auto-archive timer expires

#### Auto-Archive Monitoring

**Check auto-archive settings**:
```json5
{
  agents: {
    defaults: {
      subagents: {
        archiveAfterMinutes: 60  // Default 60 minutes
      }
    }
  }
}
```

**Auto-archive behavior**:
- Best-effort; pending timers lost on gateway restart
- Archives to `*.deleted.<timestamp>`
- Keeps transcript file (rename only)
- Affects all subagents equally (depth-1 and depth-2)

### Communication Between Main Agent and Subagents

#### Announce Flow

**How subagents report back**:

1. **Subagent completes task**
   - Runs announce step inside subagent session
   - If subagent replies exactly `ANNOUNCE_SKIP`, nothing posted

2. **Announce step execution**
   - Runs inside subagent session (not requester session)
   - Generates summary message

3. **Delivery to requester**
   - Sends via `agent` call with `deliver=true`
   - Preserves thread/topic routing when available
   - Retry with exponential backoff if delivery fails

4. **Status template** (normalized):
   ```
   Status: completed successfully | failed | timed out | unknown
   Result: [summary content from announce step]
   Notes: [error details, context]
   Runtime: [duration]
   Tokens: [input/output/total]
   Session: [sessionKey, sessionId, transcript path]
   ```

#### Delivery Resilience

**Retry mechanism**:
1. Try direct `agent` delivery with stable idempotency key
2. If fails, fallback to queue routing
3. If queue unavailable, retry with exponential backoff
4. Give up after final failure

**Best-effort nature**:
- Announce is best-effort
- If gateway restarts, pending announce work lost
- No guarantee of delivery (unlike main agent replies)

#### Context Sharing

**What subagents receive**:
- Task/prompt from sessions_spawn
- Bootstrap files: AGENTS.md + TOOLS.md only
- Main agent's auth profiles (as fallback)
- **No**: SOUL.md, IDENTITY.md, USER.md, HEARTBEAT.md, BOOTSTRAP.md

**What subagents don't receive**:
- Main session conversation history
- User context from IDENTITY.md/USER.md
- Persona from SOUL.md
- Heartbeat state

**Why**: Isolation prevents context pollution, allows specialized subagents with different personas

#### Steering Active Subagents

**When to use steer/send**:
- Subagent going in wrong direction
- Need to provide additional context
- Want to narrow/expand scope mid-task
- Correct misunderstanding

**How steering works**:
- Message injected into subagent's queue
- Queue checked after each tool call
- If message present, current assistant message skipped
- New user message injected before next assistant response

**Example steering**:
```
/subagents send #1 You're focusing too much on technical SEO. Pivot to content strategy and user experience.
```

### sessions_send for Cross-Session Messaging

#### Purpose

Send messages from one session to another without spawning a new subagent.

#### When to Use

**Internal coordination**:
- Orchestrator subagent telling worker what to do
- One session informing another of completion
- Broadcasting updates to multiple sessions

**vs sessions_spawn**:
- `sessions_send`: Existing session → Existing session
- `sessions_spawn`: Existing session → New subagent session

#### Parameters

**targetSession**: Session to send message to
**message**: Message content
**inject**: Whether to inject immediately or queue

#### Example Usage

**Orchestrator → Worker**:
```
// In orchestrator subagent
sessions_send({
  targetSession: "agent:main:subagent:abc123:subagent:def456",
  message: "Start processing keyword research for the travel industry niche",
  inject: true
})
```

**Broadcast update**:
```
sessions_send({
  targetSession: "agent:seo-writer:main",
  message: "Competitor analysis complete. 23 high-priority keywords identified.",
  inject: false  // Queue for next turn
})
```

---

## Part 3: Agent Design Patterns

### Single-Purpose vs Multi-Purpose Agents

#### Single-Purpose Agents

**Characteristics**:
- Focused on one specific task or domain
- Deep expertise in narrow area
- Simple prompts, predictable outputs
- Easier to maintain and debug
- Can use cheaper models

**Examples**:
- **Keyword Research Agent**: Only does keyword discovery
- **Content Writer Agent**: Only writes content
- **SEO Auditor Agent**: Only audits content for SEO

**Pros**:
- Predictable behavior
- Specialized tools/configuration
- Cheaper to run
- Easy to test

**Cons**:
- Requires multiple agents for complex workflows
- More orchestration overhead
- Limited flexibility

**Best for**:
- Repetitive, well-defined tasks
- High-volume operations
- Clear input/output specifications

#### Multi-Purpose Agents

**Characteristics**:
- Capable of multiple related tasks
- Broad domain knowledge
- Can adapt to different requirements
- More complex prompts and configuration

**Examples**:
- **SEO Content Agent**: Research + write + audit content
- **Digital Marketing Agent**: SEO + PPC + content + social media
- **Research Agent**: Keyword research + competitor analysis + trend analysis

**Pros**:
- Fewer agents to manage
- Can handle complex workflows end-to-end
- More flexible for varied requests

**Cons**:
- Harder to maintain
- More expensive (requires better model)
- Less predictable behavior
- Harder to test

**Best for**:
- Complex, multi-step workflows
- Tasks requiring deep integration between functions
- Low-volume, high-value operations

**Hybrid Approach** (Recommended):
- Main agent: Multi-purpose orchestrator
- Subagents: Single-purpose specialists
- Orchestrator delegates to specialists as needed

### Specialized Skills Agents

#### SEO Writer Agent

**Responsibilities**:
- Keyword research and analysis
- Search intent identification
- SEO-optimized content generation
- On-page optimization (titles, meta, headers)
- Internal linking suggestions
- Schema markup generation
- E-E-A-T integration

**Skill Dependencies**:
- searxng (for research)
- web_search (if configured)
- web_fetch (for specific articles)
- No special SEO skills needed (use general tools)

**Configuration**:
```json5
{
  agents: {
    list: [
      {
        id: "seo-writer",
        model: "anthropic/claude-sonnet-4",
        subagents: {
          model: "google-gemini/gemini-2-flash",
          maxSpawnDepth: 2,
          maxChildrenPerAgent: 5
        }
      }
    ]
  }
}
```

**Tool Policy**:
- read/write/edit (file operations)
- exec (run research scripts if needed)
- web_search/web_fetch (research)
- sessions_spawn (spawn researcher subagent)
- subagents (manage researcher subagents)
- No session tools (unless orchestrator)

#### Research Agent

**Responsibilities**:
- Web research using SearXNG or web_search
- Data gathering and synthesis
- Competitive analysis
- Trend identification
- Source verification

**Configuration**:
```json5
{
  agents: {
    list: [
      {
        id: "researcher",
        model: "google-gemini/gemini-2-flash",  // Fast research
        subagents: {
          maxSpawnDepth: 1  // Can't spawn its own subagents
        }
      }
    ]
  }
}
```

**Tool Policy**:
- web_search (Brave API or SearXNG)
- web_fetch (extract article content)
- read/write (save research findings)
- No sessions_spawn (leaf worker)

#### Editor Agent

**Responsibilities**:
- Content editing and proofreading
- SEO optimization check
- Humanization of AI content
- Grammar and style improvements
- Fact-checking

**Configuration**:
```json5
{
  agents: {
    list: [
      {
        id: "editor",
        model: "anthropic/claude-3-haiku"  // Fast editing
      }
    ]
  }
}
```

**Tool Policy**:
- read/edit/write (file operations)
- No research tools (input is text)
- No sessions_spawn (leaf worker)

### Agent Hierarchies & Delegation

#### Orchestrator Pattern (Depth 2 Enabled)

**Architecture**:
```
Main Agent (Depth 0)
  ↳ Orchestrator Subagent (Depth 1)
       ↳ Researcher Worker (Depth 2)
       ↳ Writer Worker (Depth 2)
       ↳ Editor Worker (Depth 2)
```

**Configuration**:
```json5
{
  agents: {
    defaults: {
      subagents: {
        maxSpawnDepth: 2,  // Enable nesting
        maxChildrenPerAgent: 5,
        maxConcurrent: 8
      }
    }
  }
}
```

**Flow**:
1. User sends request to main agent
2. Main agent spawns orchestrator subagent with task
3. Orchestrator breaks task into subtasks
4. Orchestrator spawns worker subagents for each subtask
5. Workers complete their tasks
6. Workers announce back to orchestrator
7. Orchestrator synthesizes results
8. Orchestrator announces back to main agent
9. Main agent delivers final result to user

**Tool Policy by Depth**:

| Depth | Can Use sessions_spawn? | Can Use subagents? | Other Session Tools? |
|-------|----------------------|---------------------|---------------------|
| 0 (Main) | Yes | Yes | Yes (all) |
| 1 (Orchestrator) | Yes | Yes | Yes (list, history, send) |
| 2 (Worker) | No | No | No |

#### Announce Chain

**Each level only sees announces from its direct children**:

```
Worker 2a (Depth 2)
  → Announces to: Orchestrator (Depth 1)

Worker 2b (Depth 2)
  → Announces to: Orchestrator (Depth 1)

Orchestrator (Depth 1)
  → Receives: Worker 2a + Worker 2b announces
  → Synthesizes results
  → Announces to: Main Agent (Depth 0)

Main Agent (Depth 0)
  → Receives: Orchestrator announce
  → Delivers to: User
```

**What each level sees**:
- Depth 2 workers: Only their own task
- Depth 1 orchestrator: Tasks of workers + their own task
- Depth 0 main: Orchestrator's synthesis + user context

#### Cascade Stop Behavior

**Stopping affects entire subtree**:

```
Main Agent sends /stop
  ↳ Stops: Orchestrator 1
       ↳ Stops: Worker 2a, Worker 2b (cascade)
  ↳ Stops: Orchestrator 2
       ↳ Stops: Worker 2c (cascade)
```

**Commands**:
- `/stop` in main chat → Stops all depth-1 + cascades to depth-2
- `/subagents kill <id>` → Stops specific subagent + cascades to children
- `/subagents kill all` → Stops all subagents + cascades

### Error Handling & Recovery

#### Error Detection

**Subagent error states**:
- **failed**: Subagent encountered unrecoverable error
- **timed out**: Hit runTimeoutSeconds limit
- **killed**: Manually stopped

**Error in announce**:
- Announce step fails
- Error included in `Notes:` field
- Status: "failed" or "unknown"

#### Error Propagation

**How errors flow up chain**:

1. **Worker (Depth 2) fails**
   - Announces back to orchestrator with status: "failed"
   - Includes error in Notes: field

2. **Orchestrator (Depth 1) receives**
   - Sees worker failed
   - Can retry, handle, or fail
   - If fails, announces to main with details

3. **Main Agent (Depth 0) receives**
   - Sees orchestrator failed
   - Decides: retry, partial delivery, or inform user

#### Recovery Strategies

**Automatic Retry** (in orchestrator):
- Failed worker → spawn replacement worker
- Same task, different approach if applicable
- Limit retry attempts (don't infinite loop)

**Partial Delivery**:
- Some workers succeed, some fail
- Deliver successful results
- Note failed tasks for manual follow-up
- Ask user how to proceed

**Inform User**:
- Clear error explanation
- What went wrong
- What was completed
- Options: retry, skip, or manual fix

#### Logging for Debugging

**Check subagent logs**:
```
/subagents log #1  // See full transcript
/subagents log #1 tools  // See only tool calls
```

**Common errors to look for**:
- Tool timeouts (tool execution took too long)
- Permission errors (denied tools)
- Invalid model/thinking level
- Run timeout exceeded
- Auth/credential issues

---

## Part 4: Agent Communication Protocol

### Main Agent ↔ Subagent Communication

#### Request Flow

**Main → Subagent (spawn)**:
```
Main Agent: sessions_spawn({
  task: "Research 2025 SEO trends",
  label: "SEO Trends Research",
  model: "gemini-flash",
  thinking: "minimal"
})
→ Returns: { status: "accepted", runId, childSessionKey }
```

**Subagent executes**:
- Receives task in bootstrap
- Works on task with available tools
- Runs announce step when complete

**Subagent → Main (announce)**:
```
Subagent runs announce step:
"Completed research on 2025 SEO trends. Key findings: AI content is 53% more effective, voice search optimization is critical..."

→ Announces back to Main Agent via agent call (deliver=true)
→ Main Agent receives: Status, Result, Notes, Stats
→ Main Agent delivers to user
```

#### Protocol for SEO Writer Agent

**Main Agent brief**:
```
User: "Write a blog post about keyword research"

Main Agent spawns SEO Writer:
sessions_spawn({
  task: "Write a comprehensive SEO-optimized blog post about keyword research. Requirements:
  - Target primary keyword: 'keyword research'
  - Include secondary keywords: 'keyword research tools', 'long-tail keywords'
  - Word count: 2000+ words
  - Optimize for featured snippets
  - Include schema markup (Article, BlogPosting)
  - Write meta title and description
  - Suggest internal links
  Output: Complete article with all SEO elements",
  label: "SEO Blog Post",
  model: "claude-sonnet-4"
})
```

**SEO Writer internal flow**:
1. Receive task from main agent
2. Spawn researcher subagent for keyword analysis
3. Spawn researcher subagent for competitor research
4. Wait for both researchers to announce
5. Synthesize research findings
6. Write content (keyword integration, structure, E-E-A-T)
7. Generate SEO elements (title, meta, schema)
8. Suggest internal linking structure
9. Announce back to main agent:
   ```
   Result: Complete SEO-optimized blog post (2,450 words)
   - Primary keyword: 'keyword research' (6 mentions)
   - Secondary keywords integrated naturally
   - Title: "Keyword Research Guide for Beginners 2025 | [Brand]"
   - Meta description: [description]
   - Schema markup: Article + BlogPosting
   - Internal links: 5 suggested
   - Featured snippet optimization: 3 PAA questions targeted
   Status: completed successfully
   ```

**Main Agent delivery**:
- Receives announce
- Formats for user (remove technical stats)
- Sends final message to user

### Quality Checklist Before Delivery

#### SEO Writer Agent Self-Check

Before announcing to main agent, SEO Writer should verify:

**Content Quality**:
- [ ] Meets word count requirement (2000+)
- [ ] All required keywords integrated naturally
- [ ] Primary keyword in H1, title, URL
- [ ] Secondary keywords in H2/H3 headers
- [ ] Long-tail keywords addressed
- [ ] No keyword stuffing

**Structure**:
- [ ] Clear H1-H3 hierarchy
- [ ] Logical flow (intro → body → FAQ → conclusion)
- [ ] Paragraphs 2-4 sentences
- [ ] Bullet points for scannability
- [ ] At least one table or list for featured snippets

**SEO Elements**:
- [ ] Title tag optimized (50-60 chars)
- [ ] Meta description optimized (150-160 chars)
- [ ] URL slug contains primary keyword
- [ ] Alt text on all images
- [ ] Internal links suggested (3-5)
- [ ] External links to authoritative sources

**E-E-A-T**:
- [ ] Personal experience/anecdotes included
- [ ] Expert perspective demonstrated
- [ ] Claims supported by data/research
- [ ] Citations provided for statistics
- [ ] Author perspective clear

**Technical SEO**:
- [ ] Schema markup generated (Article, BlogPosting)
- [ ] FAQ schema if FAQ section exists
- [ ] Breadcrumb schema if applicable
- [ ] Core Web Vitals considered (image optimization)
- [ ] Mobile-first writing (short paragraphs)

**Originality**:
- [ ] Unique insights included
- [ ] Not generic AI content
- [ ] Humanized tone and style
- [ ] Specific examples, not abstractions
- [ ] No duplicate content

**Announce Format**:
```
Result: [Concise summary of what was delivered]
- Content: [Type, length, key topics]
- SEO: [Title, meta description summary]
- Optimization: [Featured snippets, schema, links]
- E-E-A-T: [Experience, expertise demonstrated]

Status: completed successfully

Notes: [Any issues or caveats]

Runtime: [duration]
Tokens: [input/output/total]
Session: [sessionKey, transcript path]
```

#### If Checklist Fails

**Partial Delivery**:
- Announce what WAS completed
- Note what failed or needs revision
- Ask main agent for guidance

**Example**:
```
Result: Blog post draft (1,800 words) - SHORT
- Content: Draft covers keyword research basics
- SEO: Title and meta description generated
- Optimization: Featured snippet sections included
- E-E-A-T: Personal examples included

Status: completed successfully

Notes: Content is 200 words short of requirement. Recommend:
1. Expand FAQ section with 3 more PAA questions
2. Add "Advanced Techniques" section (300 words)
3. Include 2 more real-world examples

Runtime: 4m32s
Tokens: input: 4,567 / output: 2,345 / total: 6,912
```

---

## Part 5: Best Practices

### When to Use Subagents

#### Use Subagents When:

**Parallelization needed**:
- Multiple independent tasks
- Can run simultaneously
- Speed up completion

**Different expertise needed**:
- Task requires domain knowledge main agent lacks
- Specialized agent with specific tools
- Different model appropriate

**Background work**:
- Long-running task
- Don't want to block main session
- User shouldn't wait

**Isolation needed**:
- Don't want context pollution
- Need different auth profiles
- Separate tool policy

#### Direct Interaction (no subagent) When:

**Simple one-liner fixes**:
- Quick edits
- Typo corrections
- Minor adjustments

**Reading code**:
- Just viewing, not modifying
- Quick lookups

**Sending a message**:
- Single action
- No complexity

**Simple configuration**:
- One config key update
- No multi-step process

### Concurrency Management

#### Global Concurrency Cap

**Configuration**:
```json5
{
  agents: {
    defaults: {
      subagents: {
        maxConcurrent: 8  // Global limit
      }
    }
  }
}
```

**Per-Agent Limit**:
```json5
{
  agents: {
    defaults: {
      subagents: {
        maxChildrenPerAgent: 5  // Per session
      }
    }
  }
}
```

**How it works**:
- Global: At most 8 subagents running system-wide
- Per-agent: Each session can have at most 5 children
- Both limits apply simultaneously
- Queue: If at limit, spawn returns `{ status: "queued", queuePosition }`

#### Nesting Depth Limits

**maxSpawnDepth: 1** (Default):
- Main can spawn subagents
- Subagents CANNOT spawn children
- No orchestrator pattern

**maxSpawnDepth: 2** (Orchestrator enabled):
- Main can spawn orchestrators
- Orchestrators can spawn workers
- Workers CANNOT spawn children
- Recommended for most use cases

**maxSpawnDepth: 3-5** (Advanced):
- Deep nesting possible
- Complex orchestrator hierarchies
- Higher complexity and debugging difficulty

### Cost Optimization

#### Model Selection Strategy

**High-Value Tasks** (Use expensive model):
- Strategic planning
- Complex decisions
- Nuanced analysis
- Code/debugging tricky issues
- Example: Claude Sonnet, GPT-4

**Low-Value Tasks** (Use cheap model):
- Simple data fetching
- Parsing
- Formatting
- Summarization
- Example: Gemini Flash, Haiku, FlashX

**Example Flow**:
```
Main Agent (Claude Sonnet) - Plan SEO strategy
  ↳ Spawn 10 Researchers (Gemini Flash) - Parallel data gathering
  ↳ Spawn Writer (Claude Sonnet) - Quality content creation
  ↳ Spawn Editor (Haiku) - Quick proofreading
```

#### Token Management

**Reduce token usage**:
- Use `thinking: "minimal"` or `off` for simple tasks
- Set lower thinking level for subagents
- Use FlashX for data fetching
- Use Haiku for quick edits

**Monitor token costs**:
- Check stats in announce: `Tokens: input/output/total`
- Configure pricing in `models.providers.*.models[].cost`
- Auto-calculates estimated cost in announce

### Testing Subagents

#### Manual Testing

**Spawn test subagent**:
```
/subagents spawn seo-writer Write a 100-word test post about keyword research. Include primary keyword in H1 and first paragraph.
```

**Verify output**:
```
/subagents info #1  // Check status and session
/subagents log #1  // Review execution
```

#### Automated Testing

**Test with simple task**:
```
sessions_spawn({
  task: "Test task: Write 'Hello World' to /tmp/test.txt and confirm it exists",
  label: "Test Subagent"
})
```

**Check results**:
- Did subagent complete?
- Was file written correctly?
- Did announce include expected content?

---

## Summary

**OpenClaw Agent Orchestration Key Points**:

1. **sessions_spawn parameters**: task (required), label, agentId, model, thinking, runTimeoutSeconds, thread, mode, cleanup

2. **Runtime options**: "subagent" (default) vs "acp" (harness), model selection for cost optimization

3. **Agent management**: subagents tool (list, kill, log, info, send, steer, spawn), monitoring, announce flow

4. **Design patterns**: Single-purpose (specialized) vs multi-purpose (flexible), specialized skills agents, agent hierarchies, orchestrator pattern

5. **Communication protocol**: Main ↔ Subagent communication, quality checklist before delivery, error handling

6. **Best practices**: When to use subagents, concurrency management, cost optimization, testing

**SEO Writer Agent Configuration**:
- Main agent: Claude Sonnet for planning
- Subagents: Gemini Flash for research, Sonnet for writing
- maxSpawnDepth: 2 (orchestrator pattern)
- maxChildrenPerAgent: 5
- Archive after 60 minutes
- 15-minute default timeout

**Communication Flow**:
- Main agent brief → SEO Writer spawn → Researchers spawn → Workers complete → Orchestrator synthesizes → Announce back → Main agent delivers

---

*This research compiles OpenClaw documentation on agent orchestration, subagent management, and best practices for building specialized agents.*
