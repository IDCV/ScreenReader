import parser as p
import config

if __name__ == "__main__":
    # NOTE: just test functions
    path = config.PATH_TO_IMAGES.format("photo_2018-04-10_16-34-54.jpg")
    result = p.pars(p.preprocess(p.get_image(path), save_option=True), lang='rus')
    print(result.text)