def make_network4(input_shape=INPUT_SHAPE):
    return (NeuralNetwork()
            .input(input_shape)
            .conv([5, 5, 24])
            .max_pool()
            .elu() # <== ELU
            .conv([5, 5, 64])
            .max_pool()
            .elu() # <== ELU
            .flatten()
            .dense(480)
            .elu() # <== ELU
            .dense(N_CLASSES))

with Session() as session:
    pipeline = build_pipeline(preprocessors, session, make_network4(), make_adam(1.0e-3))
    learning_curve = train_evaluate(pipeline, epochs=20)
    session.save('checkpoint/network5.ckpt')

show_learning_curve(learning_curve)

with Session() as session:
    pipeline = build_pipeline(preprocessors, session, make_network3())
    session.load('checkpoint/network5.ckpt')
    pred = pipeline.predict(X_valid)
cm = confusion_matrix(y_valid, pred)
plot_confusion_matrix(cm)
print_confusion_matrix(cm)
