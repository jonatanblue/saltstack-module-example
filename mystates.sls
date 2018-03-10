/tmp/emoji.txt:
  emojify.present:
    - emotion: sad

make it happy:
  emojify.present:
    - name: /tmp/emoji.txt
    - emotion: happy

check it stayed happy:
  emojify.present:
    - name: /tmp/emoji.txt
    - emotion: happy

delete it:
    emojify.absent:
      - name: /tmp/emoji.txt
