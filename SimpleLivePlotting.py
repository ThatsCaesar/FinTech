import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import yfinance as yf
from datetime import datetime




symbol = input("Enter stock ticker: ")
symbol = str(symbol)

# Initialize an empty list to store the y-values
y_values = []
x_ticks = []
x_labels = []

# Create the figure and axis for the plot
fig, ax = plt.subplots()
line, = ax.plot([], [])  # Create an empty line plot


ax.set_title(str(symbol) + " price")
ax.set_xlabel("Index")
ax.set_ylabel("Price [USD]")


#yfinance method to get the most recent stock price
def get_current_price(ticker):
    sym = yf.Ticker(ticker)
    todays_data = sym.history(period='1d')
    return todays_data['Close'][0]
    

# Function to update the plot
def update_plot(frame, ticker):

    new_price = get_current_price(ticker)
    
    # Append the new number to the list
    y_values.append(new_price)
    
    current_time = datetime.now().strftime("%H:%M:%S")

    # Update the x and y data of the line plot
    line.set_data(range(len(y_values)), y_values)

    # Set the x-axis tick labels to the current time
    x_ticks.append([current_time])

    ax.set_xticks(range(len(x_ticks)))
    ax.set_xticklabels(x_ticks)

    # Adjust the plot limits if necessary
    ax.relim()
    ax.autoscale_view()
    
    # Return the line plot
    return line,

# Create the animation
animation = FuncAnimation(fig, update_plot, fargs=(symbol,) , interval=1000)  # Update x seconds 

plt.show()