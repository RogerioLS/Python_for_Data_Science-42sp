import os
import sys


def ft_tqdm(lst: range) -> None:
    """
    A simplified version of tqdm using yield.
    """
    total = len(lst)
    for i, item in enumerate(lst):
        # Calculate progress
        progress = i + 1
        percent = (progress / total) * 100
        
        # Get terminal size to adapt the bar
        try:
            columns, _ = os.get_terminal_size()
        except OSError:
            columns = 80
            
        # Format the components
        percent_str = f"{int(percent)}%"
        count_str = f"{progress}/{total}"
        
        # Calculate bar width: 
        # [percent] + [bar] + [count] + spaces/brackets
        # Roughly: percent(4) + space(1) + brackets(2) + space(1) + count(...)
        fixed_width = len(percent_str) + len(count_str) + 10
        bar_width = columns - fixed_width
        
        if bar_width > 0:
            filled_len = int(bar_width * progress // total)
            bar = "=" * filled_len + ">" + " " * (bar_width - filled_len)
            formatted_bar = f"{percent_str}|[{bar}]| {count_str}"
        else:
            formatted_bar = f"{percent_str} {count_str}"
            
        # Print with carriage return
        sys.stdout.write(f"\r{formatted_bar}")
        sys.stdout.flush()
        
        yield item
    
    # Final newline after completion
    print()
