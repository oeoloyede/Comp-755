# Write a C program that creates a parent process and 10 child processes. Child i (for i = 1..10) should run for approximately (i + 10) milliseconds before exiting — child 1 sleeps about 11 ms, child 2 about 12 ms, and so on. The parent must not exit until every child has finished. 

# Use fork() to create each child. Each child should sleep for its assigned duration using usleep() (usleep takes microseconds, so convert milliseconds accordingly), print its own process ID and assigned sleep time, and then exit. 

# The parent should call wait() or waitpid() once per child, printing a message each time it successfully reaps one. 

# Written explanation (use your own actual output, not a generic description): suppose the parent printed its own exit message before it had called wait()/waitpid() on every child. Using the specific process IDs from your program's output, describe what state those un-reaped children would be in, what that state is called, and why an OS textbook calls this something the parent — not the OS — is responsible for cleaning up. 

# Deliverable: source code, sample output showing all 10 children being created and reaped, and your written explanation (4–6 sentences, referencing your own PIDs). 