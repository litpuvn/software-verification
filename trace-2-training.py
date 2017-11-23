import sys

total_line = 63
if len(sys.argv) > 1:
    try:
        total_line = int(sys.argv[1])
    except:
        print("invalid total line. total_line takes default value=", total_line)


trace_file = "exec-trace.txt"
training_file = "trace-training.csv"


with open(trace_file) as lines:
    with open(training_file, 'w') as training_writer:
        # write header
        training_line = []
        for i in range(1, total_line+1):
            training_line.append("line" + str(i))

        training_line.append("mul")
        my_training_line_data = ",".join(map(str, training_line))
        training_writer.write(my_training_line_data + "\n")

        for line in lines:
            executed_lines = line.split(",")
            executed_lines = list(map(int, executed_lines))
            mul = executed_lines[len(executed_lines) - 1]

            # remove last element which is the multiplication result
            executed_lines = executed_lines[0:len(executed_lines)-1]

            training_line = []
            for i in range(1, total_line+1):
                yes_no_line = 0
                if i in executed_lines:
                    yes_no_line = 1

                training_line.append(yes_no_line)

            # append the actual result
            training_line.append(mul)
            my_training_line_data = ",".join(map(str, training_line))
            training_writer.write(my_training_line_data + "\n")

        training_writer.flush()