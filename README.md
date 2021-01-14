# Installation
```
pip install git+https://github.com/lemonwaffle/cocoapi.git#subdirectory=PythonAPI
```

# Dataset Format
## Annotations
`coco_annos.json`
```
{
    "images": [
        {
            "file_name": "00001.jpg",
            "height": 427,
            "width": 640,
            "id": 0  # Unique id for each image
        },
        ...
    ],

    "annotations": [
        {
            "area": 702,  # Area of bounding box
            "bbox": [473, 395, 38, 28],  # [topleft_x, topleft_y, width, height]
            "image_id": 0,  # The image that this annotation corresponds to
            "category_id": 0,
            "id": 0  # Unique id for each annotation
        },
        ...
    ],

    "categories": [
        {"id": 0, "name": "black_spot"},
        {"id": 1, "name": "double_stack"}
    ]
}
```

## Results / Predictions
`coco_results.json`
```
[
    {
        "image_id": 0,
        "category_id": 0,
        "bbox": [473, 395, 38, 28],  # [topleft_x, topleft_y, width, height]
        "score": 0.9  # Confidence score
    },
    ...
]
```

# Usage
See the `eval.py` file for more details.
```
python eval.py \
    --annos_path coco_annos.json \
    --results_path coco_results.json
```

# References
- https://towardsdatascience.com/breaking-down-mean-average-precision-map-ae462f623a52
- https://www.immersivelimit.com/tutorials/create-coco-annotations-from-scratch/#coco-dataset-format
