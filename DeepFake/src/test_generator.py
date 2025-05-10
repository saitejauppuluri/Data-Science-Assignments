from data_generator import ImageDataGeneratorCV

gen = ImageDataGeneratorCV('Dataset/Train', batch_size=32)

X_batch, y_batch = gen[0]
print("Batch shape:", X_batch.shape)
print("Labels:", y_batch[:5])