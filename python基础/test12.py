import unittest


class AnonymousSurvey:
    # 收集匿名调查问卷的答案
    def __init__(self, question):
        # 存储一个问题，并为存储答案做准备
        self.question = question
        self.responses = []

    # 显示调查问卷。
    def show_question(self):
        print(self.question)

    # 存储单份调查答卷
    def store_response(self, new_response):
        self.responses.append(new_response)

    # 显示收集到的所有答卷
    def show_results(self):
        print("Survey results")
        for response in self.responses:
            print(response)


def question_gen():
    # 定义一个问题，并创建一个调查。
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)
    # 显示问题并存储答案。
    my_survey.show_question()
    print("Enter 'q' at any time to quit.\n")
    while True:
        response = input("Language: ")
        if response == 'q':
            break
        my_survey.store_response(response)
    # 显示调查结果。
    print("\nThank you to everyone who participated in the survey!")
    my_survey.show_results()


def get_formatted_name(first, last):
    """生成整洁的姓名。"""
    full_name = first + " "+last
    return full_name.title()


# 测试
# class NameTestCase(unittest.TestCase):
#     def test_first_last_name(self):
#         name = get_formatted_name("li", "yunlong")
#         self.assertEqual(name, "Lz Yunlong")
#
#     def test_first_last_middle_name(self):
#         """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
#         formatted_name = get_formatted_name('wolfgang', 'mozart')
#         self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用。
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):

        self.my_survey.store_response('English')
        self.assertIn('English', self.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储。"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()


