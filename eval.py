import argparse

from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval


def main(args):
    coco_gt = COCO(args.annos_path)
    coco_dt = coco_gt.loadRes(args.results_path)

    coco_eval = COCOeval(coco_gt, coco_dt, "bbox")
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()

    # mAP @ IoU=0.2 : 0.05 : 0.5
    print(coco_eval.stats[0])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--annos_path",
        help="path to COCO annotations file",
    )
    parser.add_argument(
        "--results_path",
        help="path to COCO results file",
    )
    args = parser.parse_args()

    main(args)
