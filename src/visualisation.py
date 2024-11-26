import matplotlib.pyplot as plt

def visualise_model_over_time(df):
    #define colors to use
    col1 = 'steelblue'
    col2 = 'red'
    # define subplots
    fig, ax = plt.subplots()
    # current line
    ax.plot(df.time_s,df.current_nA, color= col1)
    # x axis label
    ax.set_xlabel('Time (s)')
    # y-axis label
    ax.set_ylabel('current_nA', color = col1)
    #define second y-axis that shares x-axis with current plot
    ax2 = ax.twinx()
    # add second glucose line
    ax2.plot(df.time_s,df.substrate_reference_mM, color= col2)
    # y-axis label
    ax2.set_ylabel('substrate_reference_mM', color = col2)

def chart_actual_v_predicted(regressor, X_test, y_test):
    y_pred = regressor.predict(X_test)
    # Prediction on training set
    plt.scatter(X_test, y_test, color = 'lightcoral')
    plt.plot(X_test, y_pred, color = 'firebrick')
    plt.title('Current/Glucose Actual vs Predicted Values')
    plt.xlabel('Glucose')
    plt.ylabel('Current')
    plt.legend()
    #(['X_train/Pred(y_test)', 'X_train/y_train'], title = 'Gluc/Current', loc='best', facecolor='white')
    plt.box(False)
    plt.show()